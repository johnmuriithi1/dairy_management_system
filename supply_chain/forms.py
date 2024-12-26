from django import forms
from .models import Supplier, Product, ProductPricing, FarmerInventory, Order, FarmerOrder, FarmerSupply, SupplierInventory

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'  # Or specify fields explicitly: ['name', 'contact_person', ...]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPricingForm(forms.ModelForm):
    class Meta:
        model = ProductPricing
        fields = '__all__'
        widgets = {
            'discount_rate': forms.NumberInput(attrs={'step': '0.01'}),  # Set step for decimals
            'unit_price': forms.NumberInput(attrs={'step': '0.01'}),
        }

class FarmerInventoryForm(forms.ModelForm):
    class Meta:
        model = FarmerInventory
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}), # Date picker
        }

class FarmerOrderForm(forms.ModelForm):
    class Meta:
        model = FarmerOrder
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=FarmerOrder.STATUS_CHOICES),
            'unit_price': forms.NumberInput(attrs={'step': '0.01'}),
            'vat_amount': forms.NumberInput(attrs={'step': '0.01'}),
            'total_cost': forms.NumberInput(attrs={'step': '0.01'}),
        }

class FarmerSupplyForm(forms.ModelForm):
    class Meta:
        model = FarmerSupply
        fields = '__all__'
        widgets = {
            'unit_price': forms.NumberInput(attrs={'step': '0.01'}),
            'vat_amount': forms.NumberInput(attrs={'step': '0.01'}),
            'total_cost': forms.NumberInput(attrs={'step': '0.01'}),
        }

class SupplierInventoryForm(forms.ModelForm):
    class Meta:
        model = SupplierInventory
        fields = '__all__'