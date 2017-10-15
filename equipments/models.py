from __future__ import unicode_literals
from polymorphic.models import PolymorphicModel

from django.db import models


class EquipmentState(PolymorphicModel):

    class meta:
        abstract =True

    def fix_equipment(self):
        raise TypeError("Not possible to fix because the equipment is " + self)

    def borrow_equipment(self):
        raise TypeError("Not passible to borrow because the equipment is " + self)

    def take_back_equipment(self):
        raise TypeError("Not possible to take back because the equipment is "+ self)

    def disable_equipment(self):
        raise TypeError("Not possible to take back because the equipment is "+ self)

class BrokenEquipment(EquipmentState):
    broken_date = models.DateField(auto_now=True)
    price_repair = models.FloatField(blank=True,null=True)

    def fix_equipment(self):
        available_equipment = AvailableEquipment()
        available_equipment.save()
        return available_equipment

    def __str__(self):
        return "Broken"

class BorrowedEquipment(EquipmentState):
    borrow_date = models.DateField(auto_now=True)
    # partner shold be from Partner Class
    partner = models.CharField(max_length=30, default="blank")

    def take_back_equipment(self):
        available_equipment = AvailableEquipment()
        available_equipment.save()
        return available_equipment

    def disable_equipment(self):
        broken_equipment = BrokenEquipment()
        broken_equipment.save()
        return broken_equipment

    def __str__(self):
        return "Borrowed"

class AvailableEquipment(EquipmentState):

    def borrow_equipment(self):
        borrowed_equipment = BorrowedEquipment()
        borrowed_equipment.save()
        return borrowed_equipment

    def disable_equipment(self):
        broken_equipment = BrokenEquipment()
        broken_equipment.save()
        return broken_equipment

    def __str__(self):
        return "Available"

class Equipment(models.Model):
    state = models.ForeignKey(EquipmentState,null=True)
    equipment_name = models.CharField(max_length=30,default="blank")
    date_danation = models.DateField(auto_now=True)

    def start_state(self):
        available = AvailableEquipment()
        available.save()
        self.state = available
        super(Equipment,self).save()

    def fix_equipment(self):
        try:
            previous_state = self.state.fix_equipment()
            self.state.delete()
            self.state = previous_state
        except TypeError:
            pass

    def borrow_equipment(self):
        try:
            previous_state = self.state.borrow_equipment() 
            self.state.delete()
            self.state = previous_state
        except TypeError:
            pass

    def take_back_equipment(self):
        try:
            previous_state = self.state.take_back_equipment()
            self.state.delete()
            self.state = previous_state
        except TypeError:
            pass

    def disable_equipment(self):
        try:
            previous_state = self.state.disable_equipment()
            self.state.delete()
            self.state = previous_state
        except TypeError:
            pass

    def __str__(self):
        return self.equipment_name
