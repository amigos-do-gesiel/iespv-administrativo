from django.conf.urls import url
from django.conf.urls import include
from donation import views

urlpatterns = [
    url(r'^registerdonation/', views.register_donation, name='register_donation'),
]
