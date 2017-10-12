from django.shortcuts import render
from .models import MinMaxFloat, Donation
from users.models import Employee, Donor, Secretary, Administrator

# authencate later!!!
def register_donation(request):
    if request.method == 'GET':
        donors = Donor.objects.all()

        return render(request, "form_donation.html", {'donors': donors} )
    else:
        pass
