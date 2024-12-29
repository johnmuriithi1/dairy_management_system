from django.shortcuts import render
from django.db.models import Sum
from .models import Income, Expense
from django.db.models.functions import TruncMonth, TruncWeek, TruncDay
from django.db.models import Count

class IncomeBySource:
    @staticmethod
    def get_income_by_source():
        return Income.objects.values('source').annotate(total_income=Sum('amount'))

class ExpenseByCategory:
    @staticmethod
    def get_expense_by_category():
        return Expense.objects.values('category__name').annotate(total_expense=Sum('amount'))

class MonthlyIncome:
    @staticmethod
    def get_monthly_income():
        return Income.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_income=Sum('amount')).order_by('month')

class MonthlyExpense:
    @staticmethod
    def get_monthly_expense():
        return Expense.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_expense=Sum('amount')).order_by('month')

class WeeklyIncome:
    @staticmethod
    def get_weekly_income():
        return Income.objects.annotate(week=TruncWeek('date')).values('week').annotate(total_income=Sum('amount')).order_by('week')

class WeeklyExpense:
    @staticmethod
    def get_weekly_expense():
        return Expense.objects.annotate(week=TruncWeek('date')).values('week').annotate(total_expense=Sum('amount')).order_by('week')

class DailyIncome:
    @staticmethod
    def get_daily_income():
        return Income.objects.annotate(day=TruncDay('date')).values('day').annotate(total_income=Sum('amount')).order_by('day')

class DailyExpense:
    @staticmethod
    def get_daily_expense():
        return Expense.objects.annotate(day=TruncDay('date')).values('day').annotate(total_expense=Sum('amount')).order_by('day')

# Income by Source View (Template)
def income_by_source(request):
    data = IncomeBySource.get_income_by_source()
    context = {'data': data}
    return render(request, 'income_by_source.html', context)

# Expense by Category View (Template)
def expense_by_category(request):
    data = ExpenseByCategory.get_expense_by_category()
    context = {'data': data}
    return render(request, 'expense_by_category.html', context)

# Monthly Income View (Template)
def monthly_income(request):
    data = MonthlyIncome.get_monthly_income()
    context = {'data': data}
    return render(request, 'monthly_income.html', context)

# Monthly Expense View (Template)
def monthly_expense(request):
    data = MonthlyExpense.get_monthly_expense()
    context = {'data': data}
    return render(request, 'monthly_expense.html', context)

# Weekly Income View (Template)
def weekly_income(request):
    data = WeeklyIncome.get_weekly_income()
    context = {'data': data}
    return render(request, 'weekly_income.html', context)

# Weekly Expense View (Template)
def weekly_expense(request):
    data = WeeklyExpense.get_weekly_expense()
    context = {'data': data}
    return render(request, 'weekly_expense.html', context)

# Daily Income View (Template)
def daily_income(request):
    data = DailyIncome.get_daily_income()
    context = {'data': data}
    return render(request, 'daily_income.html', context)

# Daily Expense View (Template)
def daily_expense(request):
    data = DailyExpense.get_daily_expense()
    context = {'data': data}
    return render(request, 'daily_expense.html', context)