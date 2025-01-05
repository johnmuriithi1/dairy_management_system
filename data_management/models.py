from django.db import models
from user_management.models import Farmer  

class LiveStockType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class LiveStock(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=None)
    livestock_type = models.ForeignKey(LiveStockType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=20, unique=True, blank=True, null=True)
    photo = models.ImageField(upload_to='animal_photos/', null=True, blank=True)
    uploaded_document = models.FileField(upload_to='animal_docs/', null=True, blank=True)

    def __str__(self):
        return self.name

class AnimalProfile(models.Model):
    livestock = models.OneToOneField(LiveStock, on_delete=models.CASCADE, related_name='profile') 
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
    livestock = models.ForeignKey(LiveStock, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    treatment = models.TextField()

class Feed(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.FloatField()



class VaccinationRecord(models.Model):
    livestock = models.ForeignKey(LiveStock, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine_name = models.CharField(max_length=100)
    date_given = models.DateField()
    administered_by = models.CharField(max_length=100, blank=True, null=True)  # Veterinarian or staff
    next_vaccination_date = models.DateField(blank=True, null=True)
    batch_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.livestock.name} - {self.vaccine_name} - {self.date_given}"

class BreedingRecord(models.Model):
    sire = models.ForeignKey(LiveStock, on_delete=models.CASCADE, related_name='sire_of', null=True, blank=True)  # Father
    dam = models.ForeignKey(LiveStock, on_delete=models.CASCADE, related_name='dam_of')  # Mother
    breeding_date = models.DateField()
    expected_birth_date = models.DateField(blank=True, null=True)
    offspring = models.ForeignKey(LiveStock, on_delete=models.SET_NULL, related_name='parent_of', null=True, blank=True) # Child
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.dam.name} bred with {self.sire.name if self.sire else 'Unknown Sire'} on {self.breeding_date}"

class DeathRecord(models.Model):
    livestock = models.OneToOneField(LiveStock, on_delete=models.CASCADE, related_name='death_record')
    date_of_death = models.DateField()
    cause_of_death = models.CharField(max_length=200, blank=True, null=True)
    disposal_method = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.livestock.name} - {self.date_of_death}"

class Event(models.Model):
    livestock = models.ForeignKey(LiveStock, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=100)  # e.g., Shearing, Calving, Weaning
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.livestock.name} - {self.event_type} - {self.date}"