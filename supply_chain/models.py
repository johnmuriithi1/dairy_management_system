from django.db import models
from user_management.models import Farmer

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Product(models.Model):
    product_code = models.CharField(max_length=20,unique=True)
    category = models.CharField(max_length=50)
    description = models.TextField()
    unit_of_measure = models.CharField(max_length=5)
    quantity_in_stock = models.PositiveIntegerField()
    minimum_stock_level = models.PositiveIntegerField()
    maximum_stock_level = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier, related_name='products', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

class ProductPricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_group = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    minimum_quantity_for_discount = models.PositiveIntegerField(null=True, blank=True)
    farmer_category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class FarmerInventory(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    minimum_stock_level = models.PositiveIntegerField()
    maximum_stock_level = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()
    

class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Complete')])
    
    def __str__(self):
        return f"Order of {self.quantity} {self.product.name}"

class FarmerOrder(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_reference = models.CharField(max_length=50)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=[])
    uploaded_document = models.FileField(upload_to='order_docs/', null=True, blank=True)

class FarmerSupply(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_reference = models.CharField(max_length=50)
    quantity_supplied = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_document = models.FileField(upload_to='supply_docs/', null=True, blank=True)

class SupplierInventory(models.Model):
    product = models.ForeignKey(Product, related_name='inventory', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"