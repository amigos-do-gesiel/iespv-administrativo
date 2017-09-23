from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from IESPV.settings import EMAIL_HOST_USER


class Employee(User):
    class Meta:
        abstract = True

    phone_number = models.CharField(max_length = 12)

    def register_donator():
        pass

    def confirm_scheduling():
        pass

    def edit_donator():
        pass

class Administrator(Employee):
    is_superuser = True

    def register_employee(employee_type, name, phone_number, email, password):
        if employee_type == 'secretary':
            user = create_secretary(name, phone_number, email, password)
        else:
            user = create_administrator(name, phone_number, email, password)
        user.save()

    def remove_employee():
        pass

    def release_login():
        pass

    def block_login():
        pass

    def create_secretary(name, phone_number, email, password):
        user = Secretary (first_name = name,
                        phone_number = phone_number,
                        username = email,
                        password = password)
        return user

    def create_administrator(name, phone_number, username, password):
        user = Administrator (first_name = name,
                            phone_number = phone_number,
                            username = email,
                            password = password)
        return user
class Secretary (Employee):
    is_superuser = False
    #List<Observer> observers: Observer

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
            super().save()
        else:
            recovery_password.token_hash = self.token_hash
            recovery_password.token_used = False
            recovery_password.save()
