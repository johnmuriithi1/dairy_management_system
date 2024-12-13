from django.db import models
from user_management.models import Farmer,FarmAgent,VeterinaryPartner

class VeterinaryVisit(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    vet = models.ForeignKey(VeterinaryPartner, on_delete=models.CASCADE)
    date = models.DateField()
    #cow = models.ForeignKey(DairyCow, on_delete=models.CASCADE)
    vet_report = models.TextField()
    uploaded_document = models.FileField(upload_to='vet_visit_docs/', null=True, blank=True)


class InseminationCalfingTracker(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateField()
    #cow = models.ForeignKey(DairyCow, on_delete=models.CASCADE)
    tasks = models.TextField()
    performed_by = models.CharField(max_length=100)


class DairyFarmerTraining(models.Model):
    booking_date = models.DateField()
    training_category = models.CharField(max_length=50)
    training_type = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    objective = models.TextField()
    training_date = models.DateField()
    training_duration = models.DurationField()
    training_program = models.FileField(upload_to='training_programs/', null=True, blank=True)
    facilitator = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    attendees = models.ManyToManyField(Farmer)
    training_materials = models.FileField(upload_to='training_materials/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Conducted', 'Conducted'), ('Not Conducted', 'Not Conducted')])
    results_feedback = models.TextField(null=True, blank=True)
    cost_of_training = models.DecimalField(max_digits=10, decimal_places=2)
    farmer_training_fee = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_document = models.FileField(upload_to='training_docs/', null=True, blank=True)

class DairyFarmerAgentCalendar(models.Model):
    agent = models.ForeignKey(FarmAgent, on_delete=models.CASCADE)
    date = models.DateField()
    visit_details = models.TextField()
    uploaded_document = models.FileField(upload_to='calendar_docs/', null=True, blank=True)