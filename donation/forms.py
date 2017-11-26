from django import forms
from users.models import Employee, Donor, Secretary, Administrator

class SearchForm(forms.Form)
    class Meta:
            donor = Donor()
            fields = ['selected_donor']
