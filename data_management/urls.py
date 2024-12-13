from django.urls import path
from .views import LivestockDetailView,LivestockListCreateView,MilkProductionDetailView,MilkProductionListCreateView

urlpatterns = [
    path('livestock/', LivestockListCreateView.as_view(), name='livestock-list-create'),
    path('livestock/<int:pk>', LivestockDetailView.as_view(), name='livestock-detail'),
    path('milk-production/', MilkProductionListCreateView.as_view(), name='milk-production-create'),
    path('milk-production/<int:pk>', MilkProductionDetailView.as_view(), name='milk-production-detail'),
]