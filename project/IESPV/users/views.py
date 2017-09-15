from django.shortcuts import render
from django.contrib.auth.models import User
from .models import RecoveryPassword

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
			recovery_password(email)

def recovery_password(email):
	recovery = RecoveryPassword.objects.get(email)
	recovery = RecoveryPassword(email)


def url_recovery(request, token):
	pass
	# metodo que troca a senha do usuário

	







