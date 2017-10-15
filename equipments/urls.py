from django.conf.urls import url
from django.conf.urls import include
from equipments import views

urlpatterns = [
    url(r'^registerequipment/', views.register_equipment, name='register_equipment'),
    url(r'^borrow_equipment/', views.borrow_equipment, name='borrow_equipment'),
    url(r'^make_borrow/(?P<id_equipment>[0-9]+)/(?P<id_partner>[0-9]+)/', views.make_borrow, name = 'make_borrow'),
    url(r'^list_equipment', views.list_equipment, name = 'list_equipment'),
    url(r'^take_back_equipment/(?P<id_equipment>[0-9]+)/', views.take_back_equipment, name = 'take_back_equipment'),

]
