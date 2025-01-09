from django.db import models
from django.utils.translation import gettext_lazy as _


# Livestock Type Model
class LivestockType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Livestock Type"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name


# Livestock Model
class Livestock(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Livestock Name"))
    livestock_type = models.ForeignKey(
        LivestockType, on_delete=models.CASCADE, related_name="livestocks", verbose_name=_("Livestock Type")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender_choices = [
        ("male", _("Male")),
        ("female", _("Female")),
    ]
    gender = models.CharField(max_length=6, choices=gender_choices, verbose_name=_("Gender"))
    unique_id = models.CharField(max_length=50, unique=True, verbose_name=_("Unique Identifier"))

    def __str__(self):
        return f"{self.name} ({self.unique_id})"


# Animal Profile Model
class AnimalProfile(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="profiles", verbose_name=_("Livestock")
    )
    health_status = models.CharField(max_length=100, verbose_name=_("Health Status"))
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Weight (kg)"))
    birth_weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name=_("Birth Weight (kg)"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notes"))

    def __str__(self):
        return f"Profile of {self.livestock}"


# Milk Production Model
class MilkProduction(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="milk_productions", verbose_name=_("Livestock")
    )
    date = models.DateField(verbose_name=_("Date"))
    quantity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Quantity (liters)"))

    def __str__(self):
        return f"Milk Production on {self.date} for {self.livestock}"


# Health Record Model
class HealthRecord(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="health_records", verbose_name=_("Livestock")
    )
    date = models.DateField(verbose_name=_("Date"))
    issue = models.CharField(max_length=255, verbose_name=_("Health Issue"))
    treatment = models.TextField(verbose_name=_("Treatment Details"))
    veterinarian = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Veterinarian"))

    def __str__(self):
        return f"Health Record for {self.livestock} on {self.date}"


# Feed Model
class Feed(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="feeds", verbose_name=_("Livestock")
    )
    date = models.DateField(verbose_name=_("Date"))
    feed_type = models.CharField(max_length=100, verbose_name=_("Feed Type"))
    quantity = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Quantity (kg)"))

    def __str__(self):
        return f"Feed for {self.livestock} on {self.date}"


# Vaccination Record Model
class VaccinationRecord(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="vaccinations", verbose_name=_("Livestock")
    )
    vaccine_name = models.CharField(max_length=100, verbose_name=_("Vaccine Name"))
    date_administered = models.DateField(verbose_name=_("Date Administered"))
    next_due_date = models.DateField(blank=True, null=True, verbose_name=_("Next Due Date"))

    def __str__(self):
        return f"Vaccination Record for {self.livestock}"


# Breeding Record Model
class BreedingRecord(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="breeding_records", verbose_name=_("Livestock")
    )
    mating_date = models.DateField(verbose_name=_("Mating Date"))
    expected_due_date = models.DateField(blank=True, null=True, verbose_name=_("Expected Due Date"))
    outcome_choices = [
        ("success", _("Success")),
        ("failure", _("Failure")),
        ("pending", _("Pending")),
    ]
    outcome = models.CharField(
        max_length=7, choices=outcome_choices, default="pending", verbose_name=_("Outcome")
    )

    def __str__(self):
        return f"Breeding Record for {self.livestock} on {self.mating_date}"


# Death Record Model
class DeathRecord(models.Model):
    livestock = models.OneToOneField(
        Livestock, on_delete=models.CASCADE, related_name="death_record", verbose_name=_("Livestock")
    )
    date = models.DateField(verbose_name=_("Date of Death"))
    cause = models.CharField(max_length=255, verbose_name=_("Cause of Death"))

    def __str__(self):
        return f"Death Record for {self.livestock}"


# Event Model
class Event(models.Model):
    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, related_name="events", verbose_name=_("Livestock")
    )
    date = models.DateField(verbose_name=_("Event Date"))
    event_type = models.CharField(max_length=100, verbose_name=_("Event Type"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return f"Event: {self.event_type} for {self.livestock} on {self.date}"
