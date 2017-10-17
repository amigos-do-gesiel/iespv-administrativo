import pytest


@pytest.mark.django_db
class TestPartners:
    
    def test_register_get(self,client):
        response = client.get('/partners/register/')
        assert response.status_code == 200

    def test_register_post(self,client):
        response = client.post('/partners/register/',{
            'name':'School',
            'description':'test test test test test test test test test test ',
            'address':'test test test test test test ',
            'fone': '1234123412',
        },follow=True)
        assert response.status_code == 200
