from rest_framework import serializers
from .models import Income, Expense, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields

class IncomeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  # Get category name

    class Meta:
        model = Income
        fields = ('id', 'source', 'amount', 'date', 'description', 'category_name')

class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)  # Get category name

    class Meta:
        model = Expense
        fields = ('id', 'category', 'amount', 'date', 'description', 'category_name')