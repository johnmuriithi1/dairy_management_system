from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model



class User(AbstractUser):
    USER_TYPE_CHOICES = [
       ( 1, 'Farmer'),
        (2, 'FarmAgent'),
        (3, 'VeterinaryPartner'),
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Farmer(models.Model):
    farmer_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    registration_date = models.DateField()
    category = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    agent = models.ForeignKey('FarmAgent', on_delete=models.SET_NULL, null=True)
    phone_contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    number_of_cows = models.PositiveIntegerField(default=0)
    geo_location = models.CharField(max_length=100)
    uploaded_document = models.FileField(upload_to='farmer_docs/', null=True, blank=True)


class FarmAgent(models.Model):
    agent_code = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=20)
    phone_contact = models.CharField(max_length=15)
    county = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    uploaded_document = models.FileField(upload_to='agent_docs/', null=True, blank=True)


class VeterinaryPartner(models.Model):
    name = models.CharField(max_length=100)
    phone_contact = models.CharField(max_length=15)