from django import forms
#from django.contrib.auth.models import User
from .models import Farmer,FarmAgent,User,VeterinaryPartner



class UserCReationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password','user_type']


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['phone_contact', 'email', 'number_of_cows', 'geo_location']


class FarmAgentForm(forms.ModelForm):
    class Meta:
        model = FarmAgent
        fields = ['agent_code', 'full_name', 'identification_number', 'phone_contact']


class VeterinaryPartnerForm(forms.ModelForm):
    class Meta:
        model = VeterinaryPartner
        fields = ['name', 'phone_contact']