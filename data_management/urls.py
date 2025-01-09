from django.urls import path
from .views import (
    LivestockTypeListView,
    create_livestock_type,
    update_livestock_type,
    LivestockListView,
    create_livestock,
    update_livestock,
    AnimalProfileListView,
    create_animal_profile,
    update_animal_profile,
    MilkProductionListView,
    create_milk_production,
    update_milk_production,
    HealthRecordListView,
    create_health_record,
    update_health_record,
    FeedListView,
    create_feed,
    update_feed,
    VaccinationRecordListView,
    create_vaccination_record,
    update_vaccination_record,
    BreedingRecordListView,
    create_breeding_record,
    update_breeding_record,
    DeathRecordListView,
    create_death_record,
    update_death_record,
    EventListView,
    create_event,
    update_event,
    delete_animal_profile,
    view_animal_profile,
    delete_milk_production
)

app_name = 'data_management'  # Set the app name for namespacing

urlpatterns = [
      # Livestock Type URLs
     path('livestock-type/', LivestockTypeListView.as_view(), name='livestock_type_list'),
     path('livestock-type/create/', create_livestock_type, name='create_livestock_type'),
     path('livestock-type/update/<int:pk>/', update_livestock_type, name='update_livestock_type'),

     # Livestock URLs
     path('livestock/', LivestockListView.as_view(), name='livestock_list'),
     path('livestock/create/', create_livestock, name='create_livestock'),
     path('livestock/update/<int:pk>/', update_livestock, name='update_livestock'),

     # Animal Profile URLs
     path('animal-profile/', AnimalProfileListView.as_view(), name='animal_profile_list'),
     path('animal-profile/create/', create_animal_profile, name='create_animal_profile'),
     path('animal-profile/update/<int:pk>/', update_animal_profile, name='update_animal_profile'),
     path('animal-profile/delete/<int:pk>/', delete_animal_profile, name='delete_animal_profile'),
     path('animal-profile/view/<int:pk>/', view_animal_profile, name='view_animal_profile'), 

     # Milk Production URLs
     path('milk-production/', MilkProductionListView.as_view(), name='milk_production_list'),
    path('milk-production/create/', create_milk_production, name='create_milk_production'),
    path('milk-production/update/<int:pk>/', update_milk_production, name='update_milk_production'),
    path('milk-production/delete/<int:pk>/', delete_milk_production, name='delete_milk_production'),

     # Health Record URLs
     path('health-record/', HealthRecordListView.as_view(), name='health_record_list'),
     path('health-record/create/', create_health_record, name='create_health_record'),
     path('health-record/update/<int:pk>/', update_health_record, name='update_health_record'),

     # Feed URLs
     path('feed/', FeedListView.as_view(), name='feed_list'),
     path('feed/create/', create_feed, name='create_feed'),
     path('feed/update/<int:pk>/', update_feed, name='update_feed'),

     # Vaccination Record URLs
     path('vaccination-record/', VaccinationRecordListView.as_view(), name='vaccination_record_list'),
     path('vaccination-record/create/', create_vaccination_record, name='create_vaccination_record'),
     path('vaccination-record/update/<int:pk>/', update_vaccination_record, name='update_vaccination_record'),

     # Breeding Record URLs
     path('breeding-record/', BreedingRecordListView.as_view(), name='breeding_record_list'),
     path('breeding-record/create/', create_breeding_record, name='create_breeding_record'),
     path('breeding-record/update/<int:pk>/', update_breeding_record, name='update_breeding_record'),

     # Death Record URLs
     path('death-record/', DeathRecordListView.as_view(), name='death_record_list'),
     path('death-record/create/', create_death_record, name='create_death_record'),
     path('death-record/update/<int:pk>/', update_death_record, name='update_death_record'),

     # Event URLs
     path('event/', EventListView.as_view(), name='event_list'),
     path('event/create/', create_event, name='create_event'),
     path('event/update/<int:pk>/', update_event, name='update_event'),
]
