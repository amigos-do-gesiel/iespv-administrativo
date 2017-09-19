from django.db import models
from django.contrib.auth.models import User


class Employee(User):
    class Meta:
        abstract = True

    phone_number = models.CharField(max_length = 12)

    def register_donator():
        pass

    def confirm_scheduling():
        pass

    def edit_donator():
        pass

class Administrator(Employee):
    is_superuser = True

    def register_employee():
        pass

    def remove_employee():
        pass

    def release_login():
        pass

    def block_login():
        pass

class Secretary (Employee):
    is_superuser = False
    #List<Observer> observers: Observer
