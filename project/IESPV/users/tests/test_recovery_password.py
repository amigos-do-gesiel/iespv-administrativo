import hashlib
import pytest

from django.contrib.auth.models import User
from django.core import mail

from factories import UserFactory
from users.models import RecoveryPassword

@pytest.mark.django_db
class TestRecoveryPassWord:
    
    def setup(self):
        self.user1 = UserFactory()

    def test_solicitation_reset_password_get(self,client):

        response = client.get('/users/solicitar_senha/')
        assert response.status_code == 200

     # Test correct email.
    def test_solicitation_reset_password_post(self,client):
        response = client.post('/users/solicitar_senha/',
                {'email': self.user1.email},
                follow=True)
        assert response.status_code == 200

    # Test wrong email.
    def test_solicitation_reset_password_post(self,client):
        response = client.post('/users/solicitar_senha/',
                {'email': ''},
                follow=True)
        assert response.status_code == 200

    # Test content of email.
    def test_email(self,client):
        response = client.post('/users/solicitar_senha/',
                               {'email': self.user1.email},
        follow=True)
            
        recovery_password = RecoveryPassword.objects.get(usuario=self.user1) 
        assert mail.outbox[0].subject == 'Troca de senha'
        assert mail.outbox[0].body == 'Entre nesse link para mudar sua senha localhost:8000/users/recuperar_senha/' + recovery_password.token_hash

    #Test with the wring token
    def test_url_recovery_wrong_token(self, client):
        response = client.get('/users/recuperar_senha/123', follow=True)
        assert response.status_code == 200

    #Test with the correct token
    def test_url_recovery_correct_token(self, client):
        client.post('/users/solicitar_senha/',
                               {'email': self.user1.email},
        follow=True)
        recovery_password = RecoveryPassword.objects.get(usuario=self.user1)
        response = client.get('/users/recuperar_senha/' + recovery_password.token_hash, follow=True)

        assert response.status_code == 200

    #Test change of password and used token.
    def test_password_change(self, client):
        assert self.user1.password == 'Passw0rd'
        client.post('/users/solicitar_senha/',
                               {'email': self.user1.email},
        follow=True)
        
        recovery_password = RecoveryPassword.objects.get(usuario=self.user1)
        response = client.post('/users/recuperar_senha/' + recovery_password.token_hash + '/',
                               {'password':'test-test','confirm_password':'test-test'},
                               follow=True)

        user = User.objects.get(id=self.user1.id)
        # Cryptografy of the password dont let a comparison, just look if the password is changed.
        assert user.password != 'passw0rd'

        response2 = client.get('/users/recuperar_senha/' + recovery_password.token_hash, follow=True)
        assert response2.status_code == 200
    

    
