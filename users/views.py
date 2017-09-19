from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from .models import Secretary, Administrator

# Create your views here.
def index(request):
    return render(request, 'index.html')

#@login_required
#@user_passes_test(lambda user: user.is_staff, login_url='/accounts/dashboard/')
def register(request):
    if request.method == "GET":
        return render(request, 'userRegister/register.html')
    else:
        form = request.POST
        employee_type = form.get('employee_type')
        name = form.get('name')
        name = form.get('name')
        phone_number = form.get('phone_number')
        email = form.get('email')
        password = form.get('password')
        confirm_password = form.get('confirmPassword')


        if employee_type == 'secretary':
            user = create_secratary(name, phone_number, email, password)
        else:
            user = create_administrator(name, phone_number, email, password)

        user.save()
        print ('sucesso!')
    return render(request, 'index.html')

def create_secratary(name, phone_number, email, password):
    user = Secretary (first_name = name,
                    phone_number=phone_number,
                    username=email,
                    password=password)
    return user

def create_administrator(name, phone_number, email, password):
    user = Administrator (first_name = name,
                        phone_number=phone_number,
                        username=email,
                        password=password)
    return user
