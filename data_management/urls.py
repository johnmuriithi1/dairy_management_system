from django.urls import path
from .views import (
    LivestockTypeListView, LivestockTypeCreateView, LivestockTypeUpdateView, LivestockTypeDeleteView,
    LivestockListView, LivestockCreateView, LivestockUpdateView, LivestockDeleteView,
    AnimalProfileListView, AnimalProfileCreateView, AnimalProfileUpdateView, AnimalProfileDeleteView,
    MilkProductionListView, MilkProductionCreateView, MilkProductionUpdateView, MilkProductionDeleteView,
    HealthRecordListView, HealthRecordCreateView, HealthRecordUpdateView, HealthRecordDeleteView,
    FeedListView, FeedCreateView, FeedUpdateView, FeedDeleteView,
    VaccinationRecordListView, VaccinationRecordCreateView, VaccinationRecordUpdateView, VaccinationRecordDeleteView,
    BreedingRecordListView, BreedingRecordCreateView, BreedingRecordUpdateView, BreedingRecordDeleteView,
    DeathRecordListView, DeathRecordCreateView, DeathRecordUpdateView, DeathRecordDeleteView,
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,AnimalProfileDetailView
)

app_name = 'data_management'  

urlpatterns = [
    # Livestock Type URLs
    path('livestock-type/', LivestockTypeListView.as_view(), name='livestock_type_list'),
    path('livestock-type/create/', LivestockTypeCreateView.as_view(), name='create_livestock_type'),
    path('livestock-type/update/<int:pk>/', LivestockTypeUpdateView.as_view(), name='update_livestock_type'),
    path('livestock-type/delete/<int:pk>/', LivestockTypeDeleteView.as_view(), name='delete_livestock_type'),

    # Livestock URLs
    path('livestock/', LivestockListView.as_view(), name='livestock_list'),
    path('livestock/create/', LivestockCreateView.as_view(), name='create_livestock'),
    path('livestock/update/<int:pk>/', LivestockUpdateView.as_view(), name='update_livestock'),
    path('livestock/delete/<int:pk>/', LivestockDeleteView.as_view(), name='delete_livestock'),

    # Animal Profile URLs
    path('animal-profiles/', AnimalProfileListView.as_view(), name='animal_profile_list'),
    path('animal-profiles/create/', AnimalProfileCreateView.as_view(), name='animal_profile_create'),
    path('animal-profile/<int:pk>/', AnimalProfileDetailView.as_view(), name='animal_profile_detail'),
    path('animal-profiles/update/<int:pk>/', AnimalProfileUpdateView.as_view(), name='animalprofile_update'),
    path('animal-profiles/delete/<int:pk>/', AnimalProfileDeleteView.as_view(), name='animalprofile_delete'),

    # Milk Production URLs
    path('milk-production/', MilkProductionListView.as_view(), name='milk_production_list'),
    path('milk-production/create/', MilkProductionCreateView.as_view(), name='create_milk_production'),
    path('milk-production/update/<int:pk>/', MilkProductionUpdateView.as_view(), name='update_milk_production'),
    path('milk-production/delete/<int:pk>/', MilkProductionDeleteView.as_view(), name='delete_milk_production'),

    # Health Record URLs
    path('health-record/', HealthRecordListView.as_view(), name='health_record_list'),
    path('health-record/create/', HealthRecordCreateView.as_view(), name='create_health_record'),
    path('health-record/update/<int:pk>/', HealthRecordUpdateView.as_view(), name='update_health_record'),
    path('health-record/delete/<int:pk>/', HealthRecordDeleteView.as_view(), name='delete_health_record'),

    # Feed URLs
    path('feed/', FeedListView.as_view(), name='feed_list'),
    path('feed/create/', FeedCreateView.as_view(), name='create_feed'),
    path('feed/update/<int:pk>/', FeedUpdateView.as_view(), name='update_feed'),
    path('feed/delete/<int:pk>/', FeedDeleteView.as_view(), name='delete_feed'),

    # Vaccination Record URLs
    path('vaccination-record/', VaccinationRecordListView.as_view(), name='vaccination_record_list'),
    path('vaccination-record/create/', VaccinationRecordCreateView.as_view(), name='create_vaccination_record'),
    path('vaccination-record/update/<int:pk>/', VaccinationRecordUpdateView.as_view(), name='update_vaccination_record'),
    path('vaccination-record/delete/<int:pk>/', VaccinationRecordDeleteView.as_view(), name='delete_vaccination_record'),

    # Breeding Record URLs
    path('breeding-record/', BreedingRecordListView.as_view(), name='breeding_record_list'),
    path('breeding-record/create/', BreedingRecordCreateView.as_view(), name='create_breeding_record'),
    path('breeding-record/update/<int:pk>/', BreedingRecordUpdateView.as_view(), name='update_breeding_record'),
    path('breeding-record/delete/<int:pk>/', BreedingRecordDeleteView.as_view(), name='delete_breeding_record'),

    # Death Record URLs
    path('death-record/', DeathRecordListView.as_view(), name='death_record_list'),
    path('death-record/create/', DeathRecordCreateView.as_view(), name='create_death_record'),
    path('death-record/update/<int:pk>/', DeathRecordUpdateView.as_view(), name='update_death_record'),
    path('death-record/delete/<int:pk>/', DeathRecordDeleteView.as_view(), name='delete_death_record'),

    # Event URLs
    path('event/', EventListView.as_view(), name='event_list'),
    path('event/create/', EventCreateView.as_view(), name='create_event'),
    path('event/update/<int:pk>/', EventUpdateView.as_view(), name='update_event'),
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='delete_event'),
]
