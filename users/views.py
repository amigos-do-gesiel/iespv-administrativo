from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from .models import Secretary, Administrator
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

#@login_required
#@user_passes_test(lambda user: user.is_staff, login_url='/accounts/dashboard/')
def register(request):
    if request.method == "GET":
        return render(request, 'usersRegister/register.html')
    else:
        form = request.POST
        employee_type = form.get('employee_type')

        #in case of error, this variable holds it's message. Otherwise it stays empty
        validation_status = validate_form(form)

        #means that the validations have found an error
        if len(validation_status) != 0 :
            return render (request,
                        'usersRegister/register.html',
                        {'falha': validation_status})


        if employee_type == 'secretary':
            user = create_secretary(form)
        else:
            user = create_administrator(form)

        user.save()

    return render(request, 'index.html')

def create_secretary(form):
    user = Secretary (first_name = form.get('name'),
                    phone_number=form.get('phone_number'),
                    username=form.get('email'),
                    password=form.get('password'))
    return user

def create_administrator(form):
    user = Administrator (first_name = form.get('name'),
                        phone_number=form.get('phone_number'),
                        username=form.get('email'),
                        password=form.get('password'))
    return user

def validate_form(form):
    name = form.get('name')
    email = form.get('email')
    password = form.get('password')
    confirm_password = form.get('confirmPassword')

    resultCheck = ''
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
