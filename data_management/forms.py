from django import forms
from .models import (
    LiveStockType, LiveStock, AnimalProfile, MilkProduction,
    HealthRecord, Feed, VaccinationRecord, BreedingRecord,
    DeathRecord, Event
)

class LiveStockTypeForm(forms.ModelForm):
    class Meta:
        model = LiveStockType
        fields = '__all__'

class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        fields = '__all__'
        widgets = {
            'date_weighted': forms.DateInput(attrs={'type': 'date'}),
        }

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = '__all__'
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date'}),
        }

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__'

class VaccinationRecordForm(forms.ModelForm):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'
        widgets = {
            'date_given': forms.DateInput(attrs={'type': 'date'}),
            'next_vaccination_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BreedingRecordForm(forms.ModelForm):
    class Meta:
        model = BreedingRecord
        fields = '__all__'
        widgets = {
            'breeding_date': forms.DateInput(attrs={'type': 'date'}),
            'expected_birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class DeathRecordForm(forms.ModelForm):
    class Meta:
        model = DeathRecord
        fields = '__all__'
        widgets = {
            'date_of_death': forms.DateInput(attrs={'type': 'date'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }