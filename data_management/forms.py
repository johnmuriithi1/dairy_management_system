from django import forms
from .models import LiveStock, AnimalProfile,MilkProduction,HealthRecord,Feed

class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = '__all__' 

class AnimalProfileForm(forms.ModelForm):
    class Meta:
        model = AnimalProfile
        fields = '__all__' 

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = '__all__'

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__'