from django import forms
from .models import (
    LivestockType,
    Livestock,
    AnimalProfile,
    MilkProduction,
    HealthRecord,
    Feed,
    VaccinationRecord,
    BreedingRecord,
    DeathRecord,
    Event,
)


# Livestock Type Form
class LivestockTypeForm(forms.ModelForm):
    class Meta:
        model = LivestockType
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter livestock type name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }


# Livestock Form
class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['name', 'livestock_type', 'gender', 'unique_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter livestock name'}),
            'livestock_type': forms.Select(attrs={'class': 'form-control'}),
           
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'unique_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique identifier'}),
        }


# Animal Profile Form
class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        fields = [
            'livestock', 'name', 'profile_photo', 'document_upload', 'date_of_birth',
            'health_status', 'weight', 'birth_weight', 'notes'
        ]
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter animal name'}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'document_upload': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'health_status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter health status'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight in kg'}),
            'birth_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter birth weight in kg'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter notes'}),
        }


# Milk Production Form
class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = ['animal_profile', 'livestock', 'quantity', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If an animal_profile is provided, prefill the livestock field
        if 'animal_profile' in self.data:
            animal_profile_id = self.data.get('animal_profile')
            if animal_profile_id:
                # Populate the livestock field based on the selected animal_profile
                animal_profile = AnimalProfile.objects.get(pk=animal_profile_id)
                self.fields['livestock'].initial = animal_profile.livestock

# Health Record Form
class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['livestock', 'date', 'issue', 'treatment', 'veterinarian']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'issue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter health issue'}),
            'treatment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter treatment details'}),
            'veterinarian': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter veterinarian name'}),
        }


# Feed Form
class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['livestock', 'date', 'feed_type', 'quantity']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'feed_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter feed type'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity in kg'}),
        }


# Vaccination Record Form
class VaccinationRecordForm(forms.ModelForm):
    class Meta:
        model = VaccinationRecord
        fields = ['livestock', 'vaccine_name', 'date_administered', 'next_due_date']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'vaccine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vaccine name'}),
            'date_administered': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


# Breeding Record Form
class BreedingRecordForm(forms.ModelForm):
    class Meta:
        model = BreedingRecord
        fields = ['livestock', 'mating_date', 'expected_due_date', 'outcome']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'mating_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expected_due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'outcome': forms.Select(attrs={'class': 'form-control'}),
        }


# Death Record Form
class DeathRecordForm(forms.ModelForm):
    class Meta:
        model = DeathRecord
        fields = ['livestock', 'date', 'cause']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cause': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cause of death'}),
        }


# Event Form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['livestock', 'date', 'event_type', 'description']
        widgets = {
            'livestock': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event type'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter event description'}),
        }
