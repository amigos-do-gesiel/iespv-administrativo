from django.conf.urls import url
from django.conf.urls import include
from partners import views

urlpatterns = [
   # url(r'^$', views.index, name="index"),
    url(r'^register/', views.register, name="register"),
    url(r'^listPartners/', views.list_partners, name="list"),
]