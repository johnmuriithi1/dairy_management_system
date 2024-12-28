from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone 




class User(AbstractUser):
    USER_TYPE_CHOICES = [
        (1, 'Farmer'),
        (2, 'FarmAgent'),
        (3, 'VeterinaryPartner'),
        (4, 'FarmWorker'),  # Added FarmWorker type
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username


class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    farmer_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now) 
    category = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    agent = models.ForeignKey('FarmAgent', on_delete=models.SET_NULL, null=True)
    phone_contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    number_of_cows = models.PositiveIntegerField(default=0)
    geo_location = models.CharField(max_length=100)
    uploaded_document = models.FileField(upload_to='farmer_docs/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class FarmAgent(models.Model):
    agent_code = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    full_name = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=20)
    phone_contact = models.CharField(max_length=15)
    county = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    uploaded_document = models.FileField(upload_to='agent_docs/', null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class VeterinaryPartner(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    phone_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class FarmWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100)
    phone_contact = models.CharField(max_length=15)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='workers') #Added farmer relationship
    employment_date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username