from __future__ import unicode_literals
from django.db import models 
from abc import ABCMeta
from django.core.mail import send_mail
from IESPV.settings import EMAIL_HOST_USER

class Observer(object):
    
    def update(self, input):
        return        

class Observable(object):
    
    def add_observers():
        return

    
    def remove_observers(self, input):
        return

    
    def notify_observers(self, input):
        pass        

class Email(object):
	
	def send_email(self, subject, message, email_destination):
		send_mail(
               subject,
               message,
               EMAIL_HOST_USER,
               [email_destination],
               fail_silently=False,
        )
