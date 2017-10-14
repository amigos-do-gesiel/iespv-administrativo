from django.conf.urls import url
from django.conf.urls import include
from donation import views

urlpatterns = [
    url(r'^registerdonation/', views.register_donation, name='register_donation'),
    url(r'^list_donations/', views.list_donations, name='list_donations'),
]
