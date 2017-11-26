from __future__ import unicode_literals

from django.db import models

# Create your models heere

class Partner(models.Model):
	
	name = models.CharField(max_length=100)
	description = models.TextField()
	address = models.TextField()
	fone = models.CharField(max_length=12)

	def save_patners(self, partner_name, partner_description, partner_address, partner_fone):
		partner = Partner(name=partner_name, description = partner_description, address = partner_address, fone = partner_fone)
		partner.save()
		
	
	def __str__(self):
                return self.name
