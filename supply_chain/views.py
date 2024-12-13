from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Supplier, Product, Order, Inventory
from .serializers import SupplierSerializer, ProductSerializer, OrderSerializer, InventorySerializer


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


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer



api_view(['GET'])
def analytics_report(request):
    # Total orders and revenue
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('product__price'))['product__price__sum']
   
    # Inventory levels
    inventory_data = Inventory.objects.values('product__name').annotate(total=Sum('quantity'))
    report = {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'inventory_levels': list(inventory_data)
    }
    return Response(report)