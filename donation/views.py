from django.shortcuts import render
from .models import Donation, EquipmentDonation, CashDonation
from django.http import HttpResponseRedirect
from users.models import Employee, Donor, Secretary, Administrator
from equipments.models import Equipment
from django.core.urlresolvers import reverse

# authencate later!!!
def register_donation(request):
    donors = Donor.objects.all()
    equipments = Equipment.objects.all()
    employee = request.user

    if request.method == 'GET':
        return render(request, "form_donation.html", {'donors': donors, 'equipments': equipments})
    else:
        form = request.POST
        donor_id = form.get('donor', None)
        if donor_id == '#':
            return render(request, 'form_donation.html', {'falha': 'É necessário selecionar um doador',
                                                'donors':donors, 'equipments':equipments})
            #return render(  request, 'userRegister/registerClient.html', {'falha': resultCheck})

        donation_type = form.get('donation_type', None)
        donor = Donor.objects.filter(id = donor_id)[0]
        observations = form.get('observations')
        collection_date = form.get('collection_date')

        if donation_type == 'donation_equip':
            equipment_id = form.get('equipment', None)
            equipment = Equipment.objects.filter(id = equipment_id)[0]
            new_eqp_donation = EquipmentDonation()
            new_eqp_donation.build_donation(equipment, donor, employee, observations, collection_date)
        else:
            value = form.get('value')
            new_cash_donation = CashDonation()
            new_cash_donation.build_donation(value, donor, employee, observations, collection_date)

    return HttpResponseRedirect(reverse('donation:list_donations'))

def list_donations(request):
    donations = Donation.objects.all()

    if request.method == 'GET':
        return render(request, "list_donations.html", {'donations': donations} )

def delete_donation(request, donation_id):
    donation = Donation.objects.filter(id=donation_id)
    donation.delete()
    return HttpResponseRedirect(reverse('donation:list_donations'))
