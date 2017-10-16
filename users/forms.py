from .models import Donor
from django.forms import ModelForm, TextInput

class DonorForm(ModelForm):
	class Meta:
		model = Donor
		fields = [
			"email",
			"donation_date",
			"phone_number",
			"address",
			"observations"
		]
		widgets = {
           'donation_date': TextInput(attrs={'class': 'form-control'}),
           'phone_number': TextInput(attrs={'class': 'form-control'}),
           'address': TextInput(attrs={'class': 'form-control'}),
           'email': TextInput(attrs={'class': 'form-control'}),
           'observations': TextInput(attrs={'class': 'form-control'}),
        }