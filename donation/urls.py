from django.conf.urls import url
from django.conf.urls import include
from donation import views

urlpatterns = [
    url(r'^registerdonation/', views.register_donation, name='register_donation'),
    url(r'^list_donations/', views.list_donations, name='list_donations'),
    url(r'^delete/(?P<donation_id>[0-9]+)/', views.delete_donation, name="delete_donation"),
    url(r'^donation_chart_year/(?P<year>[0-9]+)/', views.donation_chart_year, name="donation_chart_year"),
    url(r'^donation_chart_month/(?P<month_number>[0-9]+)/(?P<year>[0-9]+)/$', views.donation_chart_month, name = 'donation_chart_month'),
]
