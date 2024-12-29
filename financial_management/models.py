from django.db import models
from django.db.models import Sum, F

class Income(models.Model):
    source = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.source}: Ksh{self.amount}"

class Expense(models.Model):
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category}: Ksh{self.amount}"

# Create a view for total income by source
class IncomeBySource(models.Model):
    source = models.CharField(max_length=100)
    total_income = models.FloatField()

    class Meta:
        managed = False  # This view is not managed by Django ORM

    @classmethod
    def get_income_by_source(cls):
        return cls.objects.raw(
            """
            SELECT source, SUM(amount) as total_income
            FROM income
            GROUP BY source
            """
        )

# Create a view for total expense by category
class ExpenseByCategory(models.Model):
    category = models.CharField(max_length=100)
    total_expense = models.FloatField()

    class Meta:
        managed = False  # This view is not managed by Django ORM

    @classmethod
    def get_expense_by_category(cls):
        return cls.objects.raw(
            """
            SELECT category, SUM(amount) as total_expense
            FROM expense
            GROUP BY category
            """
        )

# Create a view for monthly income
class MonthlyIncome(models.Model):
    month = models.CharField(max_length=7)  # e.g., '2023-07'
    total_income = models.FloatField()

    class Meta:
        managed = False  # This view is not managed by Django ORM

    @classmethod
    def get_monthly_income(cls):
        return cls.objects.raw(
            """
            SELECT 
                strftime('%Y-%m', date) as month, 
                SUM(amount) as total_income
            FROM income
            GROUP BY month
            """
        )

# Create a view for monthly expense
class MonthlyExpense(models.Model):
    month = models.CharField(max_length=7)  # e.g., '2023-07'
    total_expense = models.FloatField()

    class Meta:
        managed = False  # This view is not managed by Django ORM

    @classmethod
    def get_monthly_expense(cls):
        return cls.objects.raw(
            """
            SELECT 
                strftime('%Y-%m', date) as month, 
                SUM(amount) as total_expense
            FROM expense
            GROUP BY month
            """
        )