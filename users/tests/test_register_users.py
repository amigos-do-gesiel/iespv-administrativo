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

    def test_register_user_get(self,client):

        response = client.get('/users/register/')
        assert response.status_code == 200
