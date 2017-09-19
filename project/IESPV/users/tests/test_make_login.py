import pytest

@pytest.mark.django_db
class TestLoginAttendant:
    def setup(self):
        pass
 
    def test_solicitation_login(self,client):
        response = client.get('/users/login/')
        assert response.status_code == 200

