from __future__ import unicode_literals

from django.db import models

class Equipament(models.Model):
    state = models.ForeingKey(EquipamentState)
    equipament_name = models.CharField()
    date_danation = models.DateField(auto_now=True)

    def fix_equipament(self):
        self.state = self.state.fix_equipament()

    def borrow_equipament(self):
        self.state = self.state.borrow_equipament() 

    def take_back_equipament(self):
        self.state = self.take_back_equipament()

    def disable_equipament(self):
        self.state = self.disable_equipament()
 
    
class EquipamentState(models.Model):
   
    class meta:
        abstract =True

    def fix_equipament(self):
        pass

    def borrow_equipament(self):
        pass

    def take_back_equipament(self):
        pass

    def disable_equipament(self):
        pass
    
    def saveState(self):
        pass

class BrokenEquipament(EquipamentState):

    def fix_equipament(self):
        pass


class BorrowedEquipament(EquipamentState):

    def take_back_equipament(self):
        pass

    def disable_equipament(self):
        pass

class AvailableEquipament(EquipamentState):

    def borrow_equipament(self):
        pass

    def disable_equipament(self):
        pass
 
