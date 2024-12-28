from django.urls import path
from . import views

app_name = 'supply_chain'
urlpatterns = [
    path('api/suppliers/', views.SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('api/suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('api/inventory/', views.FarmerInventoryListCreateView.as_view(), name='inventory-list-create'),
    path('api/inventory/<int:pk>/', views.FarmerInventoryDetailView.as_view(), name='inventory-detail'),
    path('api/analytics/report/', views.analytics_report, name='analytics-report'),


    # Supplier URLs
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),

    # Product URLs
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/pricing/', views.product_pricing_manage, name='product_pricing_manage'), #Product pricing

    # FarmerInventory URLs
    path('farmerinventories/', views.FarmerInventoryListView.as_view(), name='farmerinventory_list'),
    path('farmerinventories/create/', views.FarmerInventoryCreateView.as_view(), name='farmerinventory_create'),
    path('farmerinventories/update/<int:pk>/', views.FarmerInventoryUpdateView.as_view(), name='farmerinventory_update'),
    path('farmerinventories/delete/<int:pk>/', views.FarmerInventoryDeleteView.as_view(), name='farmerinventory_delete'),

    # Order URLs
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('orders/<int:pk>/detail/', views.order_detail, name='order_detail'), #Order detail
    path('orders/template/', views.OrderTemplateView.as_view(), name='order_template'), #Order template

    # FarmerOrder URLs
    path('farmerorders/', views.FarmerOrderListView.as_view(), name='farmerorder_list'),
    path('farmerorders/create/', views.FarmerOrderCreateView.as_view(), name='farmerorder_create'),
    path('farmerorders/update/<int:pk>/', views.FarmerOrderUpdateView.as_view(), name='farmerorder_update'),
    path('farmerorders/delete/<int:pk>/', views.FarmerOrderDeleteView.as_view(), name='farmerorder_delete'),

    # FarmerSupply URLs
    path('farmersupplies/', views.FarmerSupplyListView.as_view(), name='farmersupply_list'),
    path('farmersupplies/create/', views.FarmerSupplyCreateView.as_view(), name='farmersupply_create'),
    path('farmersupplies/update/<int:pk>/', views.FarmerSupplyUpdateView.as_view(), name='farmersupply_update'),
    path('farmersupplies/delete/<int:pk>/', views.FarmerSupplyDeleteView.as_view(), name='farmersupply_delete'),

    # SupplierInventory URLs
    path('supplierinventories/', views.SupplierInventoryListView.as_view(), name='supplierinventory_list'),
    path('supplierinventories/create/', views.SupplierInventoryCreateView.as_view(), name='supplierinventory_create'),
    path('supplierinventories/update/<int:pk>/', views.SupplierInventoryUpdateView.as_view(), name='supplierinventory_update'),
    path('supplierinventories/delete/<int:pk>/', views.SupplierInventoryDeleteView.as_view(), name='supplierinventory_delete'),
]