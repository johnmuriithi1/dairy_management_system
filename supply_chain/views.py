from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SupplierSerializer, ProductSerializer, OrderSerializer, FarmerInventorySerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Supplier, Product, ProductPricing, FarmerInventory, Order, FarmerOrder, FarmerSupply, SupplierInventory
from .forms import SupplierForm, ProductForm, ProductPricingForm, FarmerInventoryForm, OrderForm, FarmerOrderForm, FarmerSupplyForm, SupplierInventoryForm
from django.forms import inlineformset_factory
from django.urls import reverse_lazy


class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class FarmerInventoryListCreateView(generics.ListCreateAPIView):
    queryset = FarmerInventory.objects.all()
    serializer_class = FarmerInventorySerializer


class FarmerInventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmerInventory.objects.all()
    serializer_class = FarmerInventorySerializer



api_view(['GET'])
def analytics_report(request):
    # Total orders and revenue
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('product__price'))['product__price__sum']
   
    # Inventory levels
    inventory_data = FarmerInventory.objects.values('product__name').annotate(total=Sum('quantity'))
    report = {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'inventory_levels': list(inventory_data)
    }
    return Response(report)


# Supplier Views
class SupplierListView(generic.ListView):
    model = Supplier
    template_name = 'inventory/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(generic.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_form.html'
    success_url = reverse_lazy('inventory:supplier_list')

class SupplierUpdateView(generic.UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_form.html'
    success_url = reverse_lazy('inventory:supplier_list')

class SupplierDeleteView(generic.DeleteView):
    model = Supplier
    template_name = 'inventory/supplier_confirm_delete.html'
    success_url = reverse_lazy('inventory:supplier_list')

# Product Views
class ProductListView(generic.ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product_list')

class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('inventory:product_list')

class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('inventory:product_list')

# ProductPricing View with Inline Formset
ProductPricingInlineFormSet = inlineformset_factory(Product, ProductPricing, form=ProductPricingForm, extra=1, can_delete=True)

def product_pricing_manage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        formset = ProductPricingInlineFormSet(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            return redirect('inventory:product_list')
    else:
        formset = ProductPricingInlineFormSet(instance=product)
    return render(request, 'inventory/product_pricing_manage.html', {'formset': formset, 'product': product})

# FarmerInventory Views
class FarmerInventoryListView(generic.ListView):
    model = FarmerInventory
    template_name = 'inventory/farmerinventory_list.html'
    context_object_name = 'farmerinventories'

class FarmerInventoryCreateView(generic.CreateView):
    model = FarmerInventory
    form_class = FarmerInventoryForm
    template_name = 'inventory/farmerinventory_form.html'
    success_url = reverse_lazy('inventory:farmerinventory_list')

class FarmerInventoryUpdateView(generic.UpdateView):
    model = FarmerInventory
    form_class = FarmerInventoryForm
    template_name = 'inventory/farmerinventory_form.html'
    success_url = reverse_lazy('inventory:farmerinventory_list')

class FarmerInventoryDeleteView(generic.DeleteView):
    model = FarmerInventory
    template_name = 'inventory/farmerinventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:farmerinventory_list')

# Order Views
class OrderListView(generic.ListView):
    model = Order
    template_name = 'inventory/order_list.html'
    context_object_name = 'orders'

class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')

class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'
    success_url = reverse_lazy('inventory:order_list')

class OrderDeleteView(generic.DeleteView):
    model = Order
    template_name = 'inventory/order_confirm_delete.html'
    success_url = reverse_lazy('inventory:order_list')

# FarmerOrder Views
class FarmerOrderListView(generic.ListView):
    model = FarmerOrder
    template_name = 'inventory/farmerorder_list.html'
    context_object_name = 'farmerorders'

class FarmerOrderCreateView(generic.CreateView):
    model = FarmerOrder
    form_class = FarmerOrderForm
    template_name = 'inventory/farmerorder_form.html'
    success_url = reverse_lazy('inventory:farmerorder_list')

class FarmerOrderUpdateView(generic.UpdateView):
    model = FarmerOrder
    form_class = FarmerOrderForm
    template_name = 'inventory/farmerorder_form.html'
    success_url = reverse_lazy('inventory:farmerorder_list')

class FarmerOrderDeleteView(generic.DeleteView):
    model = FarmerOrder
    template_name = 'inventory/farmerorder_confirm_delete.html'
    success_url = reverse_lazy('inventory:farmerorder_list')

# FarmerSupply Views
class FarmerSupplyListView(generic.ListView):
    model = FarmerSupply
    template_name = 'inventory/farmersupply_list.html'
    context_object_name = 'farmersupplies'

class FarmerSupplyCreateView(generic.CreateView):
    model = FarmerSupply
    form_class = FarmerSupplyForm
    template_name = 'inventory/farmersupply_form.html'
    success_url = reverse_lazy('inventory:farmersupply_list')

class FarmerSupplyUpdateView(generic.UpdateView):
    model = FarmerSupply
    form_class = FarmerSupplyForm
    template_name = 'inventory/farmersupply_form.html'
    success_url = reverse_lazy('inventory:farmersupply_list')

class FarmerSupplyDeleteView(generic.DeleteView):
    model = FarmerSupply
    template_name = 'inventory/farmersupply_confirm_delete.html'
    success_url = reverse_lazy('inventory:farmersupply_list')

# SupplierInventory Views
class SupplierInventoryListView(generic.ListView):
    model = SupplierInventory
    template_name = 'inventory/supplierinventory_list.html'
    context_object_name = 'supplierinventories'

class SupplierInventoryCreateView(generic.CreateView):
    model = SupplierInventory
    form_class = SupplierInventoryForm
    template_name = 'inventory/supplierinventory_form.html'
    success_url = reverse_lazy('inventory:supplierinventory_list')

class SupplierInventoryUpdateView(generic.UpdateView):
    model = SupplierInventory
    form_class = SupplierInventoryForm
    template_name = 'inventory/supplierinventory_form.html'
    success_url = reverse_lazy('inventory:supplierinventory_list')

class SupplierInventoryDeleteView(generic.DeleteView):
    model = SupplierInventory
    template_name = 'inventory/supplierinventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:supplierinventory_list')