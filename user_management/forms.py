from django import forms
#from django.contrib.auth.models import User
from .models import Farmer,FarmAgent,User,VeterinaryPartner



class UserCReationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password', 'user_type'] 


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['phone_contact', 'email', 'number_of_cows', 'geo_location','registration_date']


class FarmAgentForm(forms.ModelForm):
    class Meta:
        model = FarmAgent
        fields = ['agent_code', 'full_name', 'identification_number', 'phone_contact']


class VeterinaryPartnerForm(forms.ModelForm):
    class Meta:
        model = VeterinaryPartner
        fields = ['name', 'phone_contact']


class FarmerProfileForm(forms.ModelForm):

    class Meta:
        model = Farmer
        fields =  ['phone_contact', 'email', 'number_of_cows', 'geo_location']


class FarmAgentProfileForm(forms.ModelForm):
    class Meta:
        model = FarmAgent
        fields =  ['agent_code', 'full_name', 'identification_number', 'phone_contact','county']


class VeterinaryPartnerProfileForm(forms.ModelForm):
    class Meta:
        model = VeterinaryPartner
        fields =  ['name', 'phone_contact']