from django.urls import path
from . import views

app_name = 'data_management'

urlpatterns = [
    # Livestock URLs
    path('livestock/', views.livestock_list, name='livestock_list'),
    path('livestock/create/', views.livestock_create, name='livestock_create'),
    path('livestock/<int:pk>/', views.livestock_detail, name='livestock_detail'),
    path('livestock/<int:pk>/edit/', views.livestock_edit, name='livestock_edit'),
    path('livestock/<int:pk>/delete/', views.livestock_delete, name='livestock_delete'),

    # Livestock Type URLs
    path('livestock/types/', views.livestock_type_list, name='livestock_type_list'),
    path('livestock/types/create/', views.livestock_type_create, name='livestock_type_create'), #Add create, detail, edit and delete for types
    path('livestock/types/<int:pk>/', views.livestock_type_detail, name='livestock_type_detail'),
    path('livestock/types/<int:pk>/edit/', views.livestock_type_edit, name='livestock_type_edit'),
    path('livestock/types/<int:pk>/delete/', views.livestock_type_delete, name='livestock_type_delete'),

    # AnimalProfile URLs
    path('animalprofile/', views.animalprofile_list, name='animalprofile_list'),
    path('animalprofile/create/', views.animalprofile_create, name='animalprofile_create'),
    path('animalprofile/<int:pk>/', views.animalprofile_detail, name='animalprofile_detail'),
    path('animalprofile/<int:pk>/edit/', views.animalprofile_edit, name='animalprofile_edit'), #Added edit
    path('animalprofile/<int:pk>/delete/', views.animalprofile_delete, name='animalprofile_delete'), #Added delete

    # MilkProduction URLs
    path('milkproduction/', views.milkproduction_list, name='milkproduction_list'),
    path('milkproduction/create/', views.milkproduction_create, name='milkproduction_create'),
    path('milkproduction/<int:pk>/', views.milkproduction_detail, name='milkproduction_detail'),
    path('milkproduction/<int:pk>/edit/', views.milkproduction_edit, name='milkproduction_edit'), #Added edit
    path('milkproduction/<int:pk>/delete/', views.milkproduction_delete, name='milkproduction_delete'), #Added delete

    # HealthRecord URLs
    path('healthrecord/', views.healthrecord_list, name='healthrecord_list'),
    path('healthrecord/create/', views.healthrecord_create, name='healthrecord_create'),
    path('healthrecord/<int:pk>/', views.healthrecord_detail, name='healthrecord_detail'),
    path('healthrecord/<int:pk>/edit/', views.healthrecord_edit, name='healthrecord_edit'), #Added edit
    path('healthrecord/<int:pk>/delete/', views.healthrecord_delete, name='healthrecord_delete'), #Added delete

    # Feed URLs
    path('feed/', views.feed_list, name='feed_list'),
    path('feed/create/', views.feed_create, name='feed_create'),
    path('feed/<int:pk>/', views.feed_detail, name='feed_detail'),
    path('feed/<int:pk>/edit/', views.feed_edit, name='feed_edit'), #Added edit
    path('feed/<int:pk>/delete/', views.feed_delete, name='feed_delete'), #Added delete

    #Vaccination Records URLs
    path('vaccinationrecord/', views.vaccinationrecord_list, name='vaccinationrecord_list'),
    path('vaccinationrecord/create/', views.vaccinationrecord_create, name='vaccinationrecord_create'),
    path('vaccinationrecord/<int:pk>/', views.vaccinationrecord_detail, name='vaccinationrecord_detail'),
    path('vaccinationrecord/<int:pk>/edit/', views.vaccinationrecord_edit, name='vaccinationrecord_edit'),
    path('vaccinationrecord/<int:pk>/delete/', views.vaccinationrecord_delete, name='vaccinationrecord_delete'),

    #Breeding Records URLs
    path('breedingrecord/', views.breedingrecord_list, name='breedingrecord_list'),
    path('breedingrecord/create/', views.breedingrecord_create, name='breedingrecord_create'),
    path('breedingrecord/<int:pk>/', views.breedingrecord_detail, name='breedingrecord_detail'),
    path('breedingrecord/<int:pk>/edit/', views.breedingrecord_edit, name='breedingrecord_edit'),
    path('breedingrecord/<int:pk>/delete/', views.breedingrecord_delete, name='breedingrecord_delete'),

    #Death Records URLs
    path('deathrecord/', views.deathrecord_list, name='deathrecord_list'),
    path('deathrecord/create/', views.deathrecord_create, name='deathrecord_create'),
    path('deathrecord/<int:pk>/', views.deathrecord_detail, name='deathrecord_detail'),
    path('deathrecord/<int:pk>/edit/', views.deathrecord_edit, name='deathrecord_edit'),
    path('deathrecord/<int:pk>/delete/', views.deathrecord_delete, name='deathrecord_delete'),

    #Event Records URLs
    path('event/', views.event_list, name='event_list'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]