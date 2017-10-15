from django.db import models
from users.models import Employee, Donor, Secretary, Administrator
from django.contrib.auth.models import AbstractUser, User
#from equipment.models import UnavalibleEquipment, BorrowedEquipment, AvalibleEquipment

# Create your models here.

class DonationStrategy(models.Model):
    pass

class Donation(models.Model):

    donor = models.ForeignKey(Donor, unique=False)
    employee = models.ForeignKey(User, blank=True, unique=False)
    strategy = models.OneToOneField(DonationStrategy,on_delete=models.CASCADE, blank= True) #there is supposed to be a DonationStrategy here

    observations = models.CharField(max_length=140)
    collection_date = models.DateField()

class CashDonation(DonationStrategy):

    donation_value = models.FloatField(blank=True)

class EquipmentDonation(DonationStrategy):
    #equipment = models.OneToManyField(Equipment)
    pass
