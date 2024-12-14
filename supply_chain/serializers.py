from rest_framework import serializers
from .models import Supplier, Product, Order, FarmerInventory


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class FarmerInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerInventory
        fields = '__all__'