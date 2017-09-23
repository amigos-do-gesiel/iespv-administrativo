import hashlib
import pytest

from django.contrib.auth.models import User
from django.core import mail

from factories import SecretaryFactory, AdministratorFactory
from users.models import Employee
from users.models import Administrator
from users.models import Secretary

@pytest.mark.django_db
class TestRegisterUsers:

    def setup(self):
        self.user1 = SecretaryFactory()
        self.user2 = AdministratorFactory()

    def test_index_get(self,client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_register_user_get(self,client):

        response = client.get('/users/register/')
        assert response.status_code == 200

    def test_register_user_secretary_post(self,client):

        response = client.post('/users/register/',{'employee_type':'secretary','name':'Marcelo', 'phone_number':'32','email':'marcelo@gmail.com', 'password':'123456789', 'confirmPassword':'123456789'}, follow = True)

        recover = Secretary.objects.get(first_name='Marcelo')

    def test_register_user_admin_post(self,client):

        response = client.post('/users/register/',{'employee_type':'admin','name':'Marco', 'phone_number':'32','email':'marco@gmail.com', 'password':'123456789', 'confirmPassword':'123456789'}, follow = True)

        recover = Administrator.objects.get(first_name='Marco')
