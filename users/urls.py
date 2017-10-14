from django.conf.urls import url
from django.conf.urls import include
from users import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^users', view.index, name="index")
    url(r'^register/', views.register, name="register"),
    url(r'^solicitar_senha/', views.solicitation_reset_password, name = 'solicitation_password'),
    url(r'^recuperar_senha/(?P<token>[0-9a-z]+)/', views.url_recovery, name = 'recovery_password'),
    url(r'^login/$', views.attendant_login, name ='login'),
    url(r'^logout/$', views.attendant_logout, name ='logout'),
    url(r'^registerdonor/', views.donor_registration, name='donor_registration'),
    url(r'^donor_profile/edit/(?P<donor_id>[0-9]+)/$', views.donor_detail, name = 'donor_detail'),
]
