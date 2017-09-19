from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import RecoveryPassword
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist

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
