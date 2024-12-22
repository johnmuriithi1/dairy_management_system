from django.urls import path
from .views import LivestockDetailView,LivestockListCreateView,MilkProductionDetailView,MilkProductionListCreateView
from . import views
urlpatterns = [
    #api views
    path('api/livestock/', LivestockListCreateView.as_view(), name='livestock-list-create'),
    path('api/livestock/<int:pk>', LivestockDetailView.as_view(), name='livestock-detail'),
    path('api/milk-production/', MilkProductionListCreateView.as_view(), name='milk-production-create'),
    path('api/milk-production/<int:pk>', MilkProductionDetailView.as_view(), name='milk-production-detail'),

    #html Views
    # Livestock URLs
    path('livestock/', views.livestock_list, name='livestock_list'),
    path('livestock/create/', views.livestock_create, name='livestock_create'),
    path('livestock/<int:pk>/', views.livestock_detail, name='livestock_detail'),

    # AnimalProfile URLs
    path('animalprofile/', views.animalprofile_list, name='animalprofile_list'),
    path('animalprofile/create/', views.animalprofile_create, name='animalprofile_create'),
    path('animalprofile/<int:pk>/', views.animalprofile_detail, name='animalprofile_detail'),

    # MilkProduction URLs
    path('milkproduction/', views.milkproduction_list, name='milkproduction_list'),
    path('milkproduction/create/', views.milkproduction_create, name='milkproduction_create'),
    path('milkproduction/<int:pk>/', views.milkproduction_detail, name='milkproduction_detail'),

    # HealthRecord URLs
    path('healthrecord/', views.healthrecord_list, name='healthrecord_list'),
    path('healthrecord/create/', views.healthrecord_create, name='healthrecord_create'),
    path('healthrecord/<int:pk>/', views.healthrecord_detail, name='healthrecord_detail'),

    # Feed URLs
    path('feed/', views.feed_list, name='feed_list'),
    path('feed/create/', views.feed_create, name='feed_create'),
    path('feed/<int:pk>/', views.feed_detail, name='feed_detail'), 
]