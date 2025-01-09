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
    Event
)

class LivestockTypeForm(forms.ModelForm):
    """Form for creating or updating LivestockType."""
    class Meta:
        model = LivestockType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LivestockForm(forms.ModelForm):
    """Form for creating or updating Livestock."""
    class Meta:
        model = Livestock
        fields = ['farmer', 'livestock_type', 'name']
        widgets = {
            'farmer': forms.Select(attrs={'class': 'form-control'}),
            'livestock_type': forms.CheckboxSelectMultiple(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AnimalProfileForm(forms.ModelForm):
    """Form for creating or updating AnimalProfile."""
    
    class Meta:
        model = AnimalProfile
        fields = ['weight', 'remarks', 'date_of_birth', 'tag', 'name', 'photo', 'uploaded_document']
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'uploaded_document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        livestock = kwargs.pop('livestock', None)
        super(AnimalProfileForm, self).__init__(*args, **kwargs)
        if livestock:
            self.fields['livestock'] = forms.ModelChoiceField(queryset=Livestock.objects.filter(pk=livestock.pk), initial=livestock)

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = ['animal', 'production_date', 'quantity_litres']
        widgets = {
            'production_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantity_litres': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs and 'animal' in kwargs['initial']:
          self.fields['animal'].widget = forms.HiddenInput()

class HealthRecordForm(forms.ModelForm):
    """Form for creating or updating HealthRecord."""
    class Meta:
        model = HealthRecord
        fields = ['animal', 'date', 'description', 'treatment']
        widgets = {
            'animal': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'treatment': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FeedForm(forms.ModelForm):
    """Form for creating or updating Feed."""
    class Meta:
        model = Feed
        fields = ['name', 'quantity', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class VaccinationRecordForm(forms.ModelForm):
    """Form for creating or updating VaccinationRecord."""
    class Meta:
        model = VaccinationRecord
        fields = ['animal', 
                  'vaccine_name', 
                  "date_given", 
                  "administered_by",
                  "next_vaccination_date",
                  "batch_number"]
        widgets = {
            "animal": forms.Select(attrs={"class": "form-control"}),
            "vaccine_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_given": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "administered_by": forms.TextInput(attrs={"class": "form-control"}),
            "next_vaccination_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "batch_number": forms.TextInput(attrs={"class": "form-control"}),
        }

class BreedingRecordForm(forms.ModelForm):
    """Form for creating or updating BreedingRecord."""
    class Meta:
        model = BreedingRecord
        fields = ['sire', 
                  "dam",
                  "breeding_date", 
                  "expected_birth_date", 
                  "offspring", 
                  "notes", 
                  "remarks"]
        widgets = {
            "sire": forms.Select(attrs={"class": "form-control"}),
            "dam": forms.Select(attrs={"class": "form-control"}),
            "breeding_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "expected_birth_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "offspring": forms.Select(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control"}),
        }

class DeathRecordForm(forms.ModelForm):
    """Form for creating or updating DeathRecord."""
    class Meta:
        model = DeathRecord
        fields = ['animal', 
                  "date_of_death", 
                  "cause_of_death", 
                  "disposal_method", 
                  "remarks"]
        widgets = {
            "animal": forms.Select(attrs={"class": "form-control"}),
            "date_of_death": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "cause_of_death": forms.TextInput(attrs={"class": "form-control"}),
            "disposal_method": forms.TextInput(attrs={"class": "form-control"}),
            "remarks": forms.Textarea(attrs={"class": "form-control"}),
        }

# Updated Event Form with Dropdown for Event Types
class EventForm(forms.ModelForm):
    """Form for creating or updating Event."""
    
    # Define choices for event types
    EVENT_TYPE_CHOICES = [
        ('shearing', 'Shearing'),
        ('calving',  'Calving'),
        ('weaning',  'Weaning'),
        ('vaccination',  'Vaccination'),
        ('breeding',  'Breeding'),
        # Add more predefined event types as needed
    ]

    # Use a ChoiceField for event_type
    event_type = forms.ChoiceField(choices=EVENT_TYPE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

    # Meta class to define model and fields
    class Meta:
        model = Event
        fields = ['animal',  'event_type',  'date',  'description',  'remarks']
        widgets = {
            'animal': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'description': forms.Textarea(attrs={'rows':'3','placeholder':'Enter event description...','class':'form-control'}),
            'remarks': forms.Textarea(attrs={'rows':'3','placeholder':'Additional remarks...','class':'form-control'}),
        }

