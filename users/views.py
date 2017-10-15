# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from .models import Secretary, Administrator, Employee, Donor
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import RecoveryPassword
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

from .forms import DonorForm

User = get_user_model()

# Create your views here.
def index(request):
    print(request.user.id)
    return render(request, 'index.html')

#The lines below must be uncommented after the merge
#@login_required
#@user_passes_test(lambda user: user.is_superuser, login_url='/accounts/dashboard/')
def register(request):

    try:
        user = User.objects.get(id=request.user.id)
        print(user)
        loggedAdmin = Administrator.objects.get(user=user)
    except ObjectDoesNotExist:
        raise Http404("Not allowed")
    except TypeError:
        raise Http404("Not allowed")

    if request.method == "GET":
        return render(request, 'usersRegister/register.html')
    else:
        form = request.POST
        #in case of error, this variable holds it's message. Otherwise it stays empty
        validation_status = validate_form(form)

        #means that the validations have found an error
        if len(validation_status) != 0 :
            return render (request,
                        'usersRegister/register.html',
                        {'falha': validation_status})

        employee_type = form.get('employee_type')
        name = form.get('name')
        email = form.get('email')
        password = form.get('password')
        phone_number = form.get('phone_number')
        loggedAdmin.register_employee(employee_type, name, phone_number, email, password)

    return render(request, 'index.html')


def validate_form(form):
    employee_type = form.get('employee_type')
    name = form.get('name')
    email = form.get('email')
    password = form.get('password')
    confirm_password = form.get('confirmPassword')

    resultCheck = ''
    resultCheck += check_employee_type_selected(employee_type)
    resultCheck += check_name(name)
    resultCheck += check_email(email)
    resultCheck += check_repeated_email(email)
    resultCheck += check_matching_passwords(password, confirm_password)

    return resultCheck

def check_name(name):
    if not name.isalpha():
        return 'Nome deve conter apenas letras  '
    else:
        return ''

def check_email(email):
    if '@' not in email or '.' not in email or ' ' in email:
        return 'Email invalido  '
    else:
        return ''

def check_repeated_email(email):
    if User.objects.filter(username=email).exists():
        return 'E-mail ja esta cadastrado no nosso banco de dados  '
    else:
        return ''

def check_matching_passwords(password, confirm_password):
    if password != confirm_password:
        return 'As senhas não combinam  '
    else:
        return ''

def check_employee_type_selected(employee_type):
    if employee_type == 'secretary':
        return ''
    elif employee_type == 'administrator':
        return ''
    else:
        return 'Você deve selecionar o tipo de funcionário  '

def solicitation_reset_password(request):
    if request.method == 'GET':
        return render(request, 'users/form_solicitation_reset_password.html')

    if request.method == 'POST':
        form = request.POST
        email = form.get('email')
        if email is None:
            return render(request, 'users/form_solicitation_reset_password.html', {"erro": "Por favor digite seu email"})
        else:
                        try:
                                recovery_password(email)
                                return render(request, 'users/verify_your_email.html')
                        except ObjectDoesNotExist:
                                return render(request, 'users/form_solicitation_reset_password.html', {"erro": "Por favor digite um email existente"})

def recovery_password(email):
        recovery = RecoveryPassword()
        recovery.send_email_url(email)

def url_recovery(request, token):
        try:
                validator = RecoveryPassword.objects.get(token_hash=token)
        except ObjectDoesNotExist:
                validator = None

        if request.method == 'GET':
                if validator is None:
                        return render(request,'users/request_token_not_exist.html')
                else:
                        if validator.token_used == False:
                                return render(request,'users/reset_password.html')
                        else:
                                return render(request,'users/used_token.html')

        elif request.method == 'POST':
                form = request.POST
                password = form.get('password')
                validator.usuario.set_password(password)
                validator.usuario.save()
                validator.token_used = True
                validator.save()
                return render(request,'users/confirm_recovery.html', {'username':validator.usuario.username})

    # metodo que troca a senha do usuário


def attendant_login(request):
    if request.method == "POST":
        login_status = make_login(request)
        if login_status.get('is_logged'):
            #TODO redirect to user profile
            login(request,login_status['user'])
            print(request.user)
            return HttpResponseRedirect(reverse('users:donors_list'))
            #return render(request,"users/login.html",login_status)
        else:
            return render(request,"users/login.html",login_status)
    else:
        return render(request,"users/login.html")

def make_login(request):
    form = request.POST
    email = form.get('email')
    password = form.get('password')

    user = authenticate(username=email, password=password)
    is_logged = False

    if user is not None:
        login(request, user)
        message = "Logged"

        is_logged = True
    else:
        message = "Incorrect user"

    context = {
        "is_logged": is_logged,
        "message": message,
        "user":user
    }

    return context

def attendant_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

#@login_required
def donor_registration(request):

    try:
        user = User.objects.get(id=request.user.id)
        print(user)
        if user.is_superuser:
            logged_employee = Administrator.objects.get(user=user)
        else:
            logged_employee = Secretary.objects.get(user=user)
    except ObjectDoesNotExist:
        raise Http404("Not allowed")
    except TypeError:
        raise Http404("Not allowed")

    if request.method == "GET":
        return render(request, 'users/form_register_donor.html')
    else:
        form = request.POST
        validation_status = donor_validate_form(form)

        if len(validation_status) != 0 :
            return render (request,
                        'users/form_register_donor.html',
                        {'falha': validation_status})

        name = form.get("name")
        phone_number = form.get("phone_number")
        address = form.get("address")
        address_reference = form.get("address_reference")
        observations = form.get("observations")
        email = form.get("email")
        donation_date = form.get("donation_date")

        logged_employee.register_donor(name, phone_number, address, address_reference, observations, email, donation_date)

    return HttpResponseRedirect(reverse('users:donors_list'))

def donor_validate_form(form):
    name = form.get('name')
    phone = form.get('phone_number')
    email = form.get('email')
    address = form.get('address')
    donation_date = form.get("donation_date")

    resultCheck = ''
    resultCheck += check_name(name)
    resultCheck += check_email(email)
    #isnt needed check for repeated email, could be both donator and functionary
    #resultCheck += check_repeated_email(email)
    return resultCheck

def donor_detail(request,donor_id):
    donor_informations = get_object_or_404(Donor, pk=donor_id)
    form = DonorForm(request.POST or None, instance=donor_informations)
    if form.is_valid():
        donor_object = form.save(commit=False)
        donor_object.save()
    return render(request,"users/donor_detail.html",{'form': form})

def donors_list(request):
    list_of_donors = Donor.objects.order_by("donation_date")
    return render(request, "users/donors_list.html",{'list_of_donors':list_of_donors})
