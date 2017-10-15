from django.shortcuts import render
from equipments.models import Equipment, AvailableEquipment, BorrowedEquipment
from equipments.models import  BrokenEquipment, EquipmentState
from users.models import Employee, Donor, Secretary, Administrator


# Create your views here.

def register_equipment(request):

    # equipment = Equipment()

    if request.method == 'GET':
        return render(request, "form_equipment.html")

    else:
        form = request.POST
        # state = form.get('state_equipment', None)
        # equipment_name = form.get('equipment_name')
        # date_danation = form.get('date')

        equipment_name = form.get('equipment_name')
        equipment = Equipment(equipment_name=equipment_name,
        state=available)
        equipment.save()
        return render(request, "index.html")
