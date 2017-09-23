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

#The lines below must be uncommented after the merge
#@login_required
#@user_passes_test(lambda user: user.is_superuser, login_url='/accounts/dashboard/')
def register(request):
    loggedAdmin = request.user

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
