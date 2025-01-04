from django import forms
from .models import LiveStock, AnimalProfile, MilkProduction, HealthRecord, Feed
from django.forms import DateInput, Select, Textarea, FileInput, NumberInput

class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = ['farmer', 'name', 'date_of_birth', 'animal_type', 'other_animal_type', 'breed', 'tag', 'photo', 'uploaded_document']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
            'animal_type': Select(choices=LiveStock.ANIMAL_TYPES),
            'photo': FileInput(attrs={'accept': 'image/*'}),
            'uploaded_document': FileInput(attrs={'accept': '.pdf,.doc,.docx'}),
        }
    breed = forms.CharField(required=False)
    tag = forms.CharField(required=False)
    photo = forms.ImageField(required=False)
    uploaded_document = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        animal_type = cleaned_data.get('animal_type')
        other_animal_type = cleaned_data.get('other_animal_type')

        if animal_type == 'other' and not other_animal_type:
            self.add_error('other_animal_type', "Please specify the animal type when 'Other' is selected.")
        elif animal_type != 'other':
            cleaned_data['other_animal_type'] = None

        return cleaned_data

class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        fields = '__all__'  # You might want to list fields explicitly here as well
        widgets = {
            'date_weighted': DateInput(attrs={'type': 'date'}),
            'remarks': Textarea(attrs={'rows': 3}),
        }

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = '__all__'  # You might want to list fields explicitly here as well
        widgets = {
            'production_date': DateInput(attrs={'type': 'date'}),
            'quantity_litres': NumberInput(attrs={'step': '0.1'}),
        }

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = '__all__'  # You might want to list fields explicitly here as well
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),  # Added widget for date field
        }

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__'  # You might want to list fields explicitly here as well