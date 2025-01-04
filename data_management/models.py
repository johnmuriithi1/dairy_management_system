from django.db import models
from user_management.models import Farmer



class LiveStock(models.Model):
    ANIMAL_TYPES = [
        ('cow', 'Cow'),
        ('goat', 'Goat'),
        ('camel', 'Camel'),
        ('sheep', 'Sheep'),
        ('other', 'Other'),  # Keep the "Other" option
    ]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    animal_type = models.CharField(max_length=20, choices=ANIMAL_TYPES, default='other')
    other_animal_type = models.CharField(max_length=50, blank=True, null=True, help_text="Specify if 'Other' is selected") # New Field
    breed = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=20, unique=True, default=None, blank=True, null=True)
    photo = models.ImageField(upload_to='animal_photos/', null=True, blank=True)
    uploaded_document = models.FileField(upload_to='animal_docs/', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self): # Add clean method for validation
        from django.core.exceptions import ValidationError
        if self.animal_type == 'other' and not self.other_animal_type:
            raise ValidationError({'other_animal_type': 'Please specify the animal type.'})
        elif self.animal_type != 'other' and self.other_animal_type:
            self.other_animal_type = None

class AnimalProfile(models.Model):
    animal = models.ForeignKey(LiveStock, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_weighted = models.DateField()
    remarks = models.TextField(null=True, blank=True)

class MilkProduction(models.Model):
    livestock = models.ForeignKey(LiveStock, related_name='milk_records', on_delete=models.CASCADE)
    production_date = models.DateField()
    quantity_litres = models.FloatField()

    def __str__(self):
        return f"{self.livestock.name}  - {self.production_date}"

class HealthRecord(models.Model):
    animal = models.ForeignKey(LiveStock, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    treatment = models.TextField()

class Feed(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.FloatField()