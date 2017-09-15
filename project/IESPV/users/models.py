from django.db import models
from django.contrib.auth.models import User
import hashlib

class RecoveryPassword(models.Model):
	usuario = models.OneToOneField(User, primary_key=True)
	token_hash = models.TextField(max_length = 60)
	date_expired = models.DateField(auto_now=True)
	token_used = models.BooleanField(False)

	def __init__(email):
		send_email_url(email)


	def search_email_user(email):
		self.send_email_url(email)

	
	def generate_hash():

		plain_text = str(self.usuario.email) + str(self.usuario.password)
		self.token_hash = hashlib.sha256(plain_text.encode('utf-8')).hexdigest()
	

	def make_url():
		return 'localhost:8000/recuperar_senha/' + token_hash 

	
	def send_email_url(email):
		self.usuario = search_email_user(email)
		self.generate_hash()
		self.make_url()


	def search_token_user():
		pass
		# verificar se o usuario já fez uma solicitação de recuperação de senha



