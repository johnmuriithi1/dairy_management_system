from django.db import models
from user_management.models import Farmer

class LiveStock(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,default='Null')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    #breed = models.ForeignKey('DairyCowBreed',null=True, on_delete=models.SET_NULL)
    cow_tag = models.CharField(max_length=20, unique=True,default='Null')
    photo = models.ImageField(upload_to='cow_photos/', null=True, blank=True)
    uploaded_document = models.FileField(upload_to='cow_docs/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class AnimalProfile(models.Model):
    name = models.ForeignKey(LiveStock, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_weighted = models.DateField()
    remarks = models.TextField(null=True, blank=True)

class AnimalBreed(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()


class MilkProduction(models.Model):
    livestock = models.ForeignKey(LiveStock,related_name='milk_records',on_delete=models.CASCADE)
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