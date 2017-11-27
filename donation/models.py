from django.db import models
from users.models import Employee, Donor, Secretary, Administrator
from django.contrib.auth.models import AbstractUser, User
from equipments.models import Equipment
from django_average.statistic_time.models import StatisticDaily, StatisticMonthly, StatisticYearly
from django_average.data_statistic.models import DataJson, DataXml

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
        self.update_donation_stats(int(value))
        new_donation = Donation(donor = donor,
                                employee = employee,
                                strategy = donation_strategy,
                                observations = observations,
                                collection_date = collection_date)
        new_donation.save()

    def get_value():
        return self.donation_subject

    def update_donation_stats(self,value):
        day = StatisticDaily()
        day.save()
        day.start()
        day.update(value)
        

class EquipmentDonation(DonationStrategy):
    donation_subject = models.ForeignKey(Equipment)

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
        return self.donation_subject.equipment_name
