from django.urls import path
from .views import SupplierListCreateView, SupplierDetailView, ProductListCreateView, ProductDetailView
from .views import OrderListCreateView, OrderDetailView, InventoryListCreateView, InventoryDetailView,analytics_report
urlpatterns = [
    path('suppliers/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('analytics/report/', analytics_report, name='analytics-report'),
]