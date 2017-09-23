from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from .models import Secretary, Administrator
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import RecoveryPassword
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

#The lines below must be uncommented after the merge
#@login_required
#@user_passes_test(lambda user: user.is_superuser, login_url='/accounts/dashboard/')
def register(request):
    loggedAdmin = Administrator.objects.get(id=request.user.id)

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
            return render(request, "/$")
        else:
            return render(request,"users/login.html",login_status)
    else:
        return render(request,"users/login.html")

def make_login(request):
    form = request.POST
    username = form.get('username')
    password = form.get('password')

    user = authenticate(username=username, password=password)
    is_logged = False

    if user is not None:
        logger = logging.getLogger(__name__)
        logger.info(user.__str__() + ' User is logged')
        login(request, user)
        message = "Logged"

        is_logged = True
    else:
        message = "Incorrect user"

    context = {
        "is_logged": is_logged,
        "message": message,
    }

    return context

def attendant_logout(request):
    logout(request)
    return render(request,"users/login.html")
