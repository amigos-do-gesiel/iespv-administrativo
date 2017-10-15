from django.conf.urls import url
from django.conf.urls import include
from equipments import views

urlpatterns = [
    url(r'^registerequipment/', views.register_equipment, name='register_equipment'),

]
