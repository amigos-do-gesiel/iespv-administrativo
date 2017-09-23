from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^solicitar_senha/', views.solicitation_reset_password, name = 'solicitation_password'),
    url(r'^recuperar_senha/(?P<token>[0-9a-f]+)/', views.url_recovery, name = 'recovery_password'),
    url(r'^login/$', views.attendant_login, name ='login'),
    url(r'^logout/$', views.attendant_logout, name ='logout'),
]
