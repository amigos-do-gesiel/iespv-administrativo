from django.db import models
from users.models import Employee, Donor, Secretary, Administrator

#from equipment.models import UnavalibleEquipment, BorrowedEquipment, AvalibleEquipment

# Create your models here.


# The class below helps to define constraints for the FloatField
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

        def formfield(self, **kwargs):
            defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
            defaults.update(kwargs)
            return super(MinMaxFloat, self).formfield(**defaults)

class Donation(models.Model):
    class Meta:
        abstract = True

    donor = models.OneToOneField(Donor)
    employee = models.OneToOneField(Secretary)

    def register_donation(self):
        pass

class CashDonation(Donation):

    donation_value = MinMaxFloat(min_value=0.0)

class EquipmentDonation(Donation):

    #equipment = models.OneToManyField(Equipment)
    pass
