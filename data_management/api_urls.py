from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

app_name = 'data_management'

router = DefaultRouter()
router.register(r'healthrecords', api_views.HealthRecordViewSet, basename='healthrecord')
router.register(r'feeds', api_views.FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('livestock/', api_views.LivestockListCreateView.as_view(), name='livestock-list-create'),
    path('livestock/<int:pk>/', api_views.LivestockDetailView.as_view(), name='livestock-detail'),
    path('milkproduction/', api_views.MilkProductionListCreateView.as_view(), name='milkproduction-list-create'),
    path('milkproduction/<int:pk>/', api_views.MilkProductionDetailView.as_view(), name='milkproduction-detail'),
]