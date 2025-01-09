from django.db import models
from django.utils import timezone
from user_management.models import Farmer  

class LivestockType(models.Model):
    """Model representing different types of livestock (e.g., cows, goats)."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Livestock(models.Model):
    """Model representing specific breeds of livestock."""
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=None)
    livestock_type = models.ManyToManyField(LivestockType, related_name='livestock') 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AnimalProfile(models.Model):
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE, related_name='profiles')
    weight = models.FloatField()
    date_weighted = models.DateField(auto_now_add=True)  # Automatically set when created
    remarks = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()
    tag = models.CharField(max_length=20, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, default="")
    photo = models.ImageField(upload_to='animal_photos/', null=True, blank=True)
    uploaded_document = models.FileField(upload_to='animal_docs/', null=True, blank=True)

    def __str__(self):
        return self.name

class MilkProduction(models.Model):
    """Model for recording milk production details for an animal."""
    animal = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='milk_records', null=True)
    production_date = models.DateField()
    quantity_litres = models.FloatField()

    def __str__(self):
        return f"{self.animal.livestock.name} - {self.production_date}"

class HealthRecord(models.Model):
    """Model for tracking health-related information for an animal."""
    animal = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='health_records', null=True)
    date = models.DateField()
    description = models.TextField()
    treatment = models.TextField()

class Feed(models.Model):
    """Model representing feed details."""
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.FloatField()

class VaccinationRecord(models.Model):
    """Model for documenting vaccination events for an animal."""
    animal = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='vaccination_records', null=True)
    vaccine_name = models.CharField(max_length=100)
    date_given = models.DateField()
    administered_by = models.CharField(max_length=100, blank=True, null=True)  # Veterinarian or staff
    next_vaccination_date = models.DateField(blank=True, null=True)
    batch_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.animal.livestock.name} - {self.vaccine_name} - {self.date_given}"

class BreedingRecord(models.Model):
    """Model for recording breeding events between animals."""
    sire = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='sire_of', null=True, blank=True)  # Father
    dam = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='dam_of')  # Mother
    breeding_date = models.DateField()
    expected_birth_date = models.DateField(blank=True, null=True)
    offspring = models.ForeignKey(Livestock, on_delete=models.SET_NULL, related_name='parent_of', null=True, blank=True)  # Child
    notes = models.TextField(blank=True, null=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.dam.name} bred with {self.sire.name if self.sire else 'Unknown Sire'} on {self.breeding_date}"

class DeathRecord(models.Model):
    """Model for tracking death events of animals."""
    animal = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='death_records', null=True)
    date_of_death = models.DateField()
    cause_of_death = models.CharField(max_length=200, blank=True, null=True)
    disposal_method = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal.livestock.name} - {self.date_of_death}"

class Event(models.Model):
    """Model for recording significant events related to animals (e.g., shearing)."""
    animal = models.ForeignKey(AnimalProfile, on_delete=models.CASCADE, related_name='event_records', null=True)
    event_type = models.CharField(max_length=100)  # e.g., Shearing, Calving
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal.livestock.name} - {self.event_type} - {self.date}"
