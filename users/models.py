from django.db import models
from django.contrib.auth.models import User


class Employee(User):

    abstract = True
    access_level

    def register_donator():
        pass

    def confirm_scheduling():
        pass

    def edit_donator():
        pass

class Administrator(Employee):

    def register_employee():
        pass

    def remove_employee():
        pass

    def release_login():
        pass

    def block_login():
        pass

class Secretary (Employee):

    #List<Observer> observers: Observer
