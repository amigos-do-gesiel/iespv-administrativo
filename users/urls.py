from django.conf.urls import url, include
from users import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^users', view.index, name="index")
    url(r'^register/', views.register, name="register"),
]
