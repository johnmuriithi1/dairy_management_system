from django import forms
from .models import Income, Expense, Category

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date', 'description', 'category', 'frequency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), # Date picker
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}), # Date picker
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']