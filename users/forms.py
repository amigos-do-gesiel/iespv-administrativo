from .models import Donor
from django.forms import ModelForm, TextInput

class DonorForm(ModelForm):
	class Meta:
			model = Donor
			fields = [
				"donation_date",
			]
			widgets = {
            'donation_date': TextInput(attrs={'class': 'form-control'}),
            }