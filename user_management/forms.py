from django import forms
#from django.contrib.auth.models import User
from .models import Farmer,FarmAgent,User,VeterinaryPartner



class UserCReationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'user_type']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

    def clean_user_type(self):
        user_type = self.cleaned_data['user_type']
        valid_user_types = [choice[0] for choice in User.USER_TYPE_CHOICES]
        if int(user_type) not in valid_user_types: #Convert user_type to int
            raise forms.ValidationError("Invalid user type selected.")
        return user_type

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


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