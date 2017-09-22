import pytest
from django.contrib.auth.models import User
from factories import UserFactory
from django.contrib import auth
import users.views
from django.contrib.auth.models import User, Permission
from django.test import Client

@pytest.mark.django_db
class TestLoginAttendant:
    def setup(self):
    	self.user1 = UserFactory()
 
    def test_solicitation_login(self,client):
        response = client.get('/users/login/')
        assert response.status_code == 200

    def test_make_login_wrong(self,client):
    	is_logged = client.login(username='asdfasdf', password='456132')
    	assert is_logged == False
    	
    def test_make_login_right(self,client):
    	response = client.post(
    		'/users/login/',
    		{"username": self.user1.username, 'password': self.user1.password},
    		follow= True)
    	assert response.status_code == 200