from django.shortcuts import render
from equipments.models import Equipment, AvailableEquipment, BorrowedEquipment
from equipments.models import  BrokenEquipment, EquipmentState
from users.models import Employee, Donor, Secretary, Administrator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from equipments.models import Equipment
from equipments.models import AvailableEquipment
from equipments.models import BorrowedEquipment
from equipments.models import BrokenEquipment
from partners.models import Partner

def register_equipment(request):

    if request.method == 'GET':
        return render(request, "form_equipment.html")

    else:
        form = request.POST
        equipment_name = form.get('equipment_name')
        equipment = Equipment()
        equipment.register_equipment(equipment_name)
        return HttpResponseRedirect(reverse('equipments:list_equipment'))

def borrow_equipment(request):
    context = {}
    if request.method == 'GET':

        all_equipments = Equipment.objects.all()
        context['all_available'] = filter(is_avalible,all_equipments)
        context['all_partners'] = Partner.objects.all()
        return render(request,'borrow_equipment/borrow_equipment.html',context)

    elif request.method == 'POST':
        form = request.POST
        equipment = form.get('equipment')
        partner = form.get('partner')

        if make_borrow(equipment,partner):
            return HttpResponseRedirect(reverse('equipments:list_equipment'))
        else:
            return render(request,'borrow_equipment/borrow_equipment_fail.html',context)

def is_avalible(Equipment):
    if type(Equipment.state) == type(AvailableEquipment()):
        return True
    else:
        return False

def is_borrow(Equipment):
    if type(Equipment.state) == type(BorrowedEquipment()):
        return True
    else:
        return False

def is_broken(Equipment):
    if type(Equipment.state) == type(BrokenEquipment()):
        return True
    else:
        return False

def make_borrow(id_equipment,id_partner):
    success = True

    try:
        equipment = Equipment.objects.get(id=id_equipment)
        partner = Partner.objects.get(id=id_partner)
    except:
        success = False

    if(is_avalible(equipment) or success):
       equipment.borrow_equipment(partner)
       equipment.save()
    else:
        success = False

    return success


def list_equipment(request):

    all_equipments = Equipment.objects.all()

    context = {
        'all_available': filter(is_avalible, all_equipments),
        'all_borrow': filter(is_borrow, all_equipments),
        'all_broken': filter(is_broken, all_equipments),
    }

    return render(request,"equipments/list_equipments.html",context)

def take_back_equipment(request,id_equipment):
    equipment = Equipment.objects.get(id=id_equipment)
    equipment.take_back_equipment()
    equipment.save()
    return HttpResponseRedirect(reverse('equipments:list_equipment'))
