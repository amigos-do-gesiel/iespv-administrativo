from django.db import models
from django.contrib.auth.models import AbstractUser, User
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from IESPV.settings import EMAIL_HOST_USER
from datetime import datetime
from six import with_metaclass
from core.models import Observer, Observable, Email 


class Employee(models.Model):
    class Meta:
        abstract = True

    phone_number = models.CharField(max_length = 12)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def register_donor(self, name, phone_number, address, address_reference, observations, email,donation_date):
        user = self.generate_user(self, name, email, '')
        donor = Donor (user=user,
                    name=name,
                    email = email,
                    phone_number=phone_number,
                    address = address,
                    address_reference = address_reference,
                    observations = observations,
                    donation_date=donation_date)
        donor.save()

    def confirm_scheduling(self):
        pass

    def edit_donor(self):
        pass

    def update_donation_date(self, newDonationDate, donor):
        donor.donation_date = newDonationDate
        donor.save()

    def __str__(self):
        return self.user.username

class Administrator(Employee, Observer):

    is_superuser = True

    def register_employee(self,employee_type, name, phone_number, email, password):
        if employee_type == 'secretary':
            self.create_secretary(name, phone_number, email, password)
        else:
            self.create_administrator(name, phone_number, email, password)

    def remove_employee(self):
        pass

    def release_login(self, id_Secretary):
        try:
            secretary = Secretary.objects.get(id=id_Secretary)
        except ObjectDoesNotExist:
            secretary = None    

        if secretary is not None:
            if secretary.activate == False:
                secretary.activate = True
                secretary.release_activate_at = datetime.now()
                secretary.save()
                release = True
            else:
                release = False
        else:
            release = False
        
        return release                    


    def block_login(self, id_Secretary):

        try:
            secretary = Secretary.objects.get(id=id_Secretary)
        except ObjectDoesNotExist:
            secretary = None    

        if secretary is not None:
            if secretary.activate == True:
                secretary.activate = False
                secretary.release_activate_at = None
                secretary.save()
                release = True
            else:
                release = False
        else:
            release = False
        
        return release

    def generate_superuser(self, name, phone_number, email, password):
        user = User(first_name=name,username=email,email=email)
        user.set_password(password)
        user.is_superuser = True
        user.save()
        return user

    def generate_user(self, name, phone_number, email, password):
        user = User(first_name=name,username=email,email=email)
        user.set_password(password)
        user.save()
        return user

    def create_secretary(self, name, phone_number, email, password):
        user = self.generate_user(self, name, email, password)
        secretary = Secretary (user=user,
                               phone_number=phone_number
        )
        secretary.save()

        return secretary

    def create_administrator(self, name, phone_number, email, password):
        user = self.generate_superuser(self, name, email, password)
        admin = Administrator (user=user,
                              phone_number=phone_number
        )
        admin.save()

        return admin

    def update(self, input):
        subject = "Login suspeito"
        message = "O Secretario dolo do email: " + input + " realizou um login agora, este email eh informativo"
        email_destination = self.user.email
        email = Email()
        email.send_email(subject, message, email_destination)
        print(email_destination)

class Secretary (Employee, Observable):
    is_superuser = False
    activate =  models.BooleanField(default=False)
    release_activate_at = models.DateTimeField(null=True, blank=True)
    observers_in_secretary = []

    def listAllSecretaries(self):
        secretaries = Secretary.objects.all()
        return secretaries

    def add_observers(self):
        self.observers_in_secretary = Administrator.objects.all()
        
    def remove_observers(self, input):
        return

    def notify_observers(self, input):
        for observer in self.observers_in_secretary:
            observer.update(input)


    def date_time_release(self):
        date_now = datetime.now()

        if self.release_activate_at.date() == date_now.date():
           if self.release_activate_at.hour - date_now.hour >= 6:
                self.add_observers()
                self.notify_observers(self.user.email) 

        else:
            self.add_observers()
            self.notify_observers(self.user.email)
        

class RecoveryPassword(models.Model):
    usuario = models.OneToOneField(User, primary_key=True,blank=True)
    token_hash = models.TextField(max_length = 60,blank=True)
    date_expired = models.DateField(auto_now=True)
    token_used = models.BooleanField(default=False)


    def search_email_user(self, email):
        self.usuario = User.objects.get(email=email)


    def generate_hash(self):

        plain_text = str(self.usuario.email) + str(self.usuario.password +str(self.date_expired))
        self.token_hash = hashlib.sha256(plain_text.encode('utf-8')).hexdigest()


    def make_url(self):
        return 'localhost:8000/users/recuperar_senha/' + str(self.token_hash)


    def send_email_url(self, email):
        self.search_email_user(email)
        self.generate_hash()
        self.search_token_user()
        self.make_url()
        send_mail(
               'Troca de senha',
               'Entre nesse link para mudar sua senha ' + self.make_url(),
                EMAIL_HOST_USER,
                [self.usuario.email],
                fail_silently=False,
        )


    def search_token_user(self):
        try:
            recovery_password = RecoveryPassword.objects.get(usuario=self.usuario)
        except ObjectDoesNotExist:
            recovery_password = None

        if recovery_password is None:
            super(RecoveryPassword,self).save()
        else:
            recovery_password.token_hash = self.token_hash
            recovery_password.token_used = False
            recovery_password.save()

class Donor (models.Model):
    name = models.CharField(max_length = 50, blank = False)
    phone_number = models.CharField(max_length = 12)
    email = models.CharField(max_length = 30, blank = True)
    address = models.CharField(max_length = 200)
    address_reference = models.CharField(max_length = 200, blank = True)
    observations = models.TextField(blank = True)
    donation_date = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
