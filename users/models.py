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

    def register_employee(employee_type, name, phone_number, email, password):
        if employee_type == 'secretary':
            user = create_secretary(name, phone_number, email, password)
        else:
            user = create_administrator(name, phone_number, email, password)
        user.save()

    def remove_employee():
        pass

    def release_login():
        pass

    def block_login():
        pass

    def create_secretary(name, phone_number, email, password):
        user = Secretary (first_name = name,
                        phone_number = phone_number,
                        username = email,
                        password = password)
        return user

    def create_administrator(name, phone_number, username, password):
        user = Administrator (first_name = name,
                            phone_number = phone_number,
                            username = email,
                            password = password)
        return user
class Secretary (Employee):
    is_superuser = False
    #List<Observer> observers: Observer
