from django.urls import path
from . import views

app_name = 'data_management'

urlpatterns = [
    # Livestock
    path('livestock/', views.livestock_list, name='livestock_list'),
    path('livestock/create/', views.livestock_create, name='livestock_create'),
    path('livestock/<int:pk>/', views.livestock_detail, name='livestock_detail'),
    path('livestock/<int:pk>/update/', views.livestock_update, name='livestock_update'),  # Use 'update'
    path('livestock/<int:pk>/delete/', views.livestock_delete, name='livestock_delete'),

    # Livestock Type
    path('livestock/types/', views.livestock_type_list, name='livestock_type_list'),
    path('livestock/types/create/', views.livestock_type_create, name='livestock_type_create'),
    path('livestock/types/<int:pk>/', views.livestock_type_detail, name='livestock_type_detail'),
    path('livestock/types/<int:pk>/update/', views.livestock_type_update, name='livestock_type_update'),  # Use 'update'
    path('livestock/types/<int:pk>/delete/', views.livestock_type_delete, name='livestock_type_delete'),

    # AnimalProfile
    path('animalprofile/', views.animalprofile_list, name='animalprofile_list'),
    path('animalprofile/livestock/<int:livestock_pk>/', views.animalprofile_list, name='animalprofile_livestock_list'),
    path('animalprofile/create/', views.animalprofile_create, name='animalprofile_create'),
    path('animalprofile/<int:pk>/', views.animalprofile_detail, name='animalprofile_detail'),  # Correct line
    path('animalprofile/<int:pk>/update/', views.animalprofile_update, name='animalprofile_update'),
    path('animalprofile/<int:pk>/delete/', views.animalprofile_delete, name='animalprofile_delete'),

    # MilkProduction
    path('milkproduction/', views.milkproduction_list, name='milkproduction_list'), #General List
    path('milkproduction/livestock/<int:livestock_pk>/', views.milkproduction_list, name='milkproduction_livestock_list'), #Filtered List
    path('milkproduction/create/', views.milkproduction_create, name='milkproduction_create'),
    path('milkproduction/<int:pk>/', views.milkproduction_detail, name='milkproduction_detail'),
    path('milkproduction/<int:pk>/update/', views.milkproduction_update, name='milkproduction_update'),  # Use 'update'
    path('milkproduction/<int:pk>/delete/', views.milkproduction_delete, name='milkproduction_delete'),

    # HealthRecord
    path('healthrecord/', views.healthrecord_list, name='healthrecord_list'), #General List
    path('healthrecord/livestock/<int:livestock_pk>/', views.healthrecord_list, name='healthrecord_livestock_list'), #Filtered List
    path('healthrecord/create/', views.healthrecord_create, name='healthrecord_create'),
    path('healthrecord/<int:pk>/', views.healthrecord_detail, name='healthrecord_detail'),
    path('healthrecord/<int:pk>/update/', views.healthrecord_update, name='healthrecord_update'),  # Use 'update'
    path('healthrecord/<int:pk>/delete/', views.healthrecord_delete, name='healthrecord_delete'),

    # Feed
    path('feed/', views.feed_list, name='feed_list'),
    path('feed/create/', views.feed_create, name='feed_create'),
    path('feed/<int:pk>/', views.feed_detail, name='feed_detail'),
    path('feed/<int:pk>/update/', views.feed_update, name='feed_update'),  # Use 'update'
    path('feed/<int:pk>/delete/', views.feed_delete, name='feed_delete'),

    # VaccinationRecord
    path('vaccinationrecord/', views.vaccinationrecord_list, name='vaccinationrecord_list'),
    path('vaccinationrecord/create/', views.vaccinationrecord_create, name='vaccinationrecord_create'),
    path('vaccinationrecord/<int:pk>/', views.vaccinationrecord_detail, name='vaccinationrecord_detail'),
    path('vaccinationrecord/<int:pk>/update/', views.vaccinationrecord_update, name='vaccinationrecord_update'),  # Use 'update'
    path('vaccinationrecord/<int:pk>/delete/', views.vaccinationrecord_delete, name='vaccinationrecord_delete'),

    # BreedingRecord
    path('breedingrecord/', views.breedingrecord_list, name='breedingrecord_list'),
    path('breedingrecord/create/', views.breedingrecord_create, name='breedingrecord_create'),
    path('breedingrecord/<int:pk>/', views.breedingrecord_detail, name='breedingrecord_detail'),
    path('breedingrecord/<int:pk>/update/', views.breedingrecord_update, name='breedingrecord_update'),  # Use 'update'
    path('breedingrecord/<int:pk>/delete/', views.breedingrecord_delete, name='breedingrecord_delete'),

    # DeathRecord
    path('deathrecord/', views.deathrecord_list, name='deathrecord_list'),
    path('deathrecord/create/', views.deathrecord_create, name='deathrecord_create'),
    path('deathrecord/<int:pk>/', views.deathrecord_detail, name='deathrecord_detail'),
    path('deathrecord/<int:pk>/update/', views.deathrecord_update, name='deathrecord_update'),  # Use 'update'
    path('deathrecord/<int:pk>/delete/', views.deathrecord_delete, name='deathrecord_delete'),

    # Event
    path('event/', views.event_list, name='event_list'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/update/', views.event_update, name='event_update'),  # Use 'update'
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]