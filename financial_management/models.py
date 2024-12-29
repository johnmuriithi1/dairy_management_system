from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Income(models.Model):
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='incomes', null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.source}: {self.amount}"

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative.")


class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.category}: {self.amount}"

    def clean(self):
        if self.amount < 0:
            raise ValidationError("Amount cannot be negative.")