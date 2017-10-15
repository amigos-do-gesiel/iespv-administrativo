from django.shortcuts import render
from equipments.models import Equipment, AvailableEquipment

# Create your views here.

def borrow_equipment(request):
    context = {}
    if request.method == 'GET':
        
        all_equipments = Equipment.objects.all()
    #    print(all_equipments[0].state)
        context['all_available'] = filter(is_avalible,all_equipments)
        print(context['all_available'])
        return render(request,'borrow_equipment/borrow_equipment.html',context)

    elif request.method == 'POST':
        form = request.POST
        equipment = form.get('equipment')
        partner = form.get('partner')

        if make_borrow():
            return render(request,'borrow_equipment/borrow_equipment.html',context)
        else:
            return render(request,'borrow_equipment/borrow_equipment_fail.html',context)
        
def is_avalible(Equipment):
    if type(Equipment.state) == type(AvailableEquipment()):
        return True
    else:
        return False
    

def make_borrow(id_equipment,id_partner):
    success = True
    
    try:
        equipment = Equipment.objects.get(id=id_equipment)
        #partner = Partner.objects.get(id=id_partner)
    except:
        success = False

    if(is_avalible(Equipment) or success):
       pass 

    else:
        success = False

    return success
        
           
