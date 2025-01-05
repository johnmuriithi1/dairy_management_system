from django import forms
from datetime import date
from .models import (
    LiveStockType, LiveStock, AnimalProfile, MilkProduction,
    HealthRecord, Feed, VaccinationRecord, BreedingRecord,
    DeathRecord, Event
)
from user_management.models import Farmer


class LiveStockTypeForm(forms.ModelForm):
    class Meta:
        model = LiveStockType
        fields = '__all__'


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class LiveStockForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user.is_superuser:
            self.fields['farmer'].queryset = Farmer.objects.all()
        else:
            self.fields['farmer'].queryset = Farmer.objects.filter(user=user)
        self.fields['livestock_type'].queryset = LiveStockType.objects.all()
        self.fields['farmer'].label = "Farmer"
        self.fields['livestock_type'].label = "Livestock Type"

    class Meta:
        model = LiveStock
        fields = ['farmer', 'livestock_type', 'name']
        widgets = {
            'farmer': forms.Select(attrs={'class': 'select2'}),
            'livestock_type': forms.Select(attrs={'class': 'select2'}),
        }


class AnimalProfileForm(forms.ModelForm):
    livestock_type = forms.ModelChoiceField(queryset=LiveStockType.objects.all(), required=True, label="Livestock Type")

    class Meta:
        model = AnimalProfile
        fields = ['livestock_type', 'name', 'weight', 'date_weighted', 'remarks', 'date_of_birth', 'tag', 'photo', 'uploaded_document']
        widgets = {
            'date_weighted': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = '__all__'
        widgets = {
            'production_date': DatePickerInput(),
        }


class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(),
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
            'date_given': DatePickerInput(),
            'next_vaccination_date': DatePickerInput(),
        }


class BreedingRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sire'].queryset = AnimalProfile.objects.all()
        self.fields['dam'].queryset = AnimalProfile.objects.all()
        self.fields['offspring'].queryset = LiveStock.objects.all()

    class Meta:
        model = BreedingRecord
        fields = '__all__'
        widgets = {
            'breeding_date': DatePickerInput(),
            'expected_birth_date': DatePickerInput(),
        }


class DeathRecordForm(forms.ModelForm):
    class Meta:
        model = DeathRecord
        fields = '__all__'
        widgets = {
            'date_of_death': DatePickerInput(),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(),
        }