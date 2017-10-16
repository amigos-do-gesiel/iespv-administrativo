from django.db import models
from users.models import Employee, Donor, Secretary, Administrator
from django.contrib.auth.models import AbstractUser, User
#from equipment.models import UnavalibleEquipment, BorrowedEquipment, AvalibleEquipment

# Create your models here.

class DonationStrategy(models.Model):
    def build_donation():
        pass

    def get_value():
        pass

class Donation(models.Model):

    donor = models.ForeignKey(Donor, unique=False)
    employee = models.ForeignKey(User, blank=True, unique=False)
    observations = models.CharField(max_length=140, blank=True)
    collection_date = models.DateField(blank=True)
    strategy = models.OneToOneField(DonationStrategy,on_delete=models.CASCADE, blank= True)

class CashDonation(DonationStrategy):

    donation_subject = models.FloatField(blank=True)

    def build_donation(self, value, donor, employee, observations, collection_date):
        donation_strategy = CashDonation(donation_subject = value)
        donation_strategy.save()
        new_donation = Donation(donor = donor,
                                employee = employee,
                                strategy = donation_strategy,
                                observations = observations,
                                collection_date = collection_date)
        new_donation.save()

    def get_value():
        return self.donation_subject

class EquipmentDonation(DonationStrategy):
    #donation_subject = models.OneToManyField(Equipment)
    donation_subject = models.CharField(max_length=140, blank=True)

    def build_donation(self, equipment, donor, employee, observations, collection_date):
        donation_strategy = EquipmentDonation(donation_subject = equipment)
        donation_strategy.save()
        new_donation = Donation(donor = donor,
                                employee = employee,
                                strategy = donation_strategy,
                                observations = observations,
                                collection_date = collection_date)
        new_donation.save()

    def get_value():
        return self.donation_subject #this will change to equipment.description
