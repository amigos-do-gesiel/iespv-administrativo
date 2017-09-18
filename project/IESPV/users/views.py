from django.shortcuts import render
from django.contrib.auth.models import User
from .models import RecoveryPassword
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

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

	







