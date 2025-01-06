from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from itertools import groupby
from django.db.models import Prefetch
from .models import (
    LiveStockType, LiveStock, AnimalProfile, MilkProduction,
    HealthRecord, Feed, VaccinationRecord, BreedingRecord,
    DeathRecord, Event 
)
from .forms import (
    LiveStockTypeForm, LiveStockForm, AnimalProfileForm, MilkProductionForm,
    HealthRecordForm, FeedForm, VaccinationRecordForm, BreedingRecordForm,
    DeathRecordForm, EventForm
)

# Generic Views (DRY - Don't Repeat Yourself)

def create_object(request, model, form_class, template_name, redirect_url):
    """Generic view for creating objects."""
    if request.method == 'POST':
        form = form_class(request.user, request.POST, request.FILES) if 'user' in form_class.__init__.__code__.co_varnames else form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  # Save without committing M2M data
            instance.save() #Save the instance first to get an id
            form.save_m2m() # Save the many to many data
            messages.success(request, f'{model._meta.verbose_name} created successfully!')

            # Determine redirect based on redirect_url
            if redirect_url.endswith('_list'):  # Check if it's a list URL
                return redirect(redirect_url)
            elif redirect_url.endswith('_create'):
                return redirect(redirect_url)
            else:  # Assume it's a detail URL (or something requiring pk)
                return redirect(redirect_url, pk=instance.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = form_class(request.user) if 'user' in form_class.__init__.__code__.co_varnames else form_class()
    return render(request, template_name, {'form': form})


def update_object(request, model, form_class, template_name, redirect_url, pk):
    """Generic view for updating objects."""
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.user, request.POST, request.FILES, instance=obj) if 'user' in form_class.__init__.__code__.co_varnames else form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model._meta.verbose_name} updated successfully!')
            return redirect(redirect_url, pk=obj.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = form_class(request.user, instance=obj) if 'user' in form_class.__init__.__code__.co_varnames else form_class(instance=obj)
    return render(request, template_name, {'form': form, model._meta.model_name: obj})


def delete_object(request, model, redirect_url, template_name, pk):
    """Generic view for deleting objects."""
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"{model._meta.verbose_name} deleted successfully.")
        return redirect(redirect_url)
    return render(request, template_name, {model._meta.model_name: obj})


def list_objects(request, model, template_name):
    """Generic view for listing objects."""
    objects = model.objects.all()
    return render(request, template_name, {model._meta.model_name + 's': objects})


def detail_object(request, model, template_name, pk):
    """Generic view for detail view of objects"""
    obj = get_object_or_404(model, pk=pk)
    return render(request, template_name, {model._meta.model_name:obj})


# AnimalProfile
def animalprofile_list(request, livestock_pk=None):
    if livestock_pk:
        try:
            livestock = LiveStock.objects.get(pk=livestock_pk)
            animalprofiles = AnimalProfile.objects.filter(livestock=livestock) #Correct way to filter
        except LiveStock.DoesNotExist:
            # Handle the case where the livestock doesn't exist.
            animalprofiles = AnimalProfile.objects.none() # Return empty queryset
            messages.error(request, "Livestock not found.")
    else:
        animalprofiles = AnimalProfile.objects.all()
    return render(request, 'livestock/animalprofile_list.html', {'animalprofiles': animalprofiles})

def animalprofile_create(request):
    if request.method == 'POST':
        form = AnimalProfileForm(request.user, request.POST, request.FILES) #Pass the user here
        if form.is_valid():
            animal_profile = form.save(commit=False)
            animal_profile.save()
            messages.success(request, 'Animal Profile created successfully!')
            return redirect('data_management:animalprofile_detail', pk=animal_profile.pk)
        else:
            return render(request, 'livestock/animalprofile_form.html', {'form': form})
    else:
        form = AnimalProfileForm(request.user) #Pass the user here
    return render(request, 'livestock/animalprofile_form.html', {'form': form})

def animalprofile_detail(request, pk):
    animalprofile = get_object_or_404(AnimalProfile, pk=pk)  # Ensure you're fetching the object
    context = {'animalprofile': animalprofile} #Correct way of passing the context
    return render(request, 'livestock/animalprofile_detail.html', context)

def animalprofile_update(request, pk):
    return update_object(request, AnimalProfile, AnimalProfileForm, 'livestock/animalprofile_form.html', 'data_management:animalprofile_detail', pk)

def animalprofile_delete(request, pk):
    return delete_object(request, AnimalProfile, 'data_management:animalprofile_list', 'livestock/animalprofile_confirm_delete.html', pk)

# MilkProduction
def milkproduction_list(request, livestock_pk=None):
    if livestock_pk:
        milkproductions = MilkProduction.objects.filter(livestock_id=livestock_pk)
    else:
        milkproductions = MilkProduction.objects.all()
    return render(request, 'milkproduction/milkproduction_list.html', {'milkproductions': milkproductions})

def milkproduction_create(request):
    return create_object(request, MilkProduction, MilkProductionForm, 'milkproduction/milkproduction_form.html', 'data_management:milkproduction_list')

def milkproduction_detail(request, pk):
    return detail_object(request, MilkProduction, 'milkproduction/milkproduction_detail.html', pk)

def milkproduction_update(request, pk):
    return update_object(request, MilkProduction, MilkProductionForm, 'milkproduction/milkproduction_form.html', 'data_management:milkproduction_detail', pk)

def milkproduction_delete(request, pk):
    return delete_object(request, MilkProduction, 'data_management:milkproduction_list', 'milkproduction/milkproduction_confirm_delete.html', pk)

# HealthRecord
def healthrecord_list(request, livestock_pk=None):
    if livestock_pk:
        healthrecords = HealthRecord.objects.filter(livestock_id=livestock_pk)
    else:
        healthrecords = HealthRecord.objects.all()
    return render(request, 'healthrecord/healthrecord_list.html', {'healthrecords': healthrecords})

def healthrecord_create(request):
    return create_object(request, HealthRecord, HealthRecordForm, 'healthrecord/healthrecord_form.html', 'data_management:healthrecord_list')

def healthrecord_detail(request, pk):
    return detail_object(request, HealthRecord, 'healthrecord/healthrecord_detail.html', pk)

def healthrecord_update(request, pk):
    return update_object(request, HealthRecord, HealthRecordForm, 'healthrecord/healthrecord_form.html', 'data_management:healthrecord_detail', pk)

def healthrecord_delete(request, pk):
    return delete_object(request, HealthRecord, 'data_management:healthrecord_list', 'healthrecord/healthrecord_confirm_delete.html')

#LiveStock
def livestock_list(request):
    livestock = LiveStock.objects.all().order_by('name').prefetch_related(Prefetch('livestock_type'), Prefetch('profiles')) #Correct way to prefetch
    livestock_grouped = []
    for livestock_instance in livestock:
        for livestock_type in livestock_instance.livestock_type.all():
            profile = livestock_instance.profiles.first()
            livestock_grouped.append({
                'livestock_type': livestock_type,
                'name': livestock_instance.name,
                'profile': profile,
            })
    context = {'livestock_grouped': livestock_grouped}
    return render(request, 'livestock/livestock_list.html', context)


def livestock_create(request):
   return create_object(request, LiveStock, LiveStockForm, 'livestock/livestock_form.html', 'data_management:livestock_list')

def livestock_detail(request, pk):
    return detail_object(request, LiveStock, 'livestock/livestock_detail.html', pk)

def livestock_update(request, pk):
    return update_object(request, LiveStock, LiveStockForm, 'livestock/livestock_form.html', 'data_management:livestock_detail', pk)


def livestock_delete(request, pk):
    return delete_object(request, LiveStock, 'data_management:livestock_list', 'livestock/livestock_confirm_delete.html', pk)


# LiveStockType Views
def livestock_type_list(request):
    return list_objects(request, LiveStockType, 'livestock/livestock_type_list.html')

def livestock_type_create(request):
    return create_object(request, LiveStockType, LiveStockTypeForm, 'livestock/livestock_type_form.html', 'data_management:livestock_type_list')

def livestock_type_detail(request, pk):
    livestock_type = get_object_or_404(LiveStockType, pk=pk)
    livestock_of_type = LiveStock.objects.filter(livestock_type=livestock_type)
    animal_profiles = []
    for livestock in livestock_of_type:
        try:
            profile = AnimalProfile.objects.get(livestock=livestock)
            animal_profiles.append(profile)
        except AnimalProfile.DoesNotExist:
            animal_profiles.append(None)  # Append None if no profile
    zipped_data = zip(livestock_of_type, animal_profiles)
    context = {
        'livestock_type': livestock_type,
        'zipped_data': zipped_data, # Pass the zipped data
        'has_livestock':livestock_of_type.exists()
    }
    return render(request, 'livestock/livestock_type_detail.html', context)

def livestock_type_update(request, pk):
    return update_object(request, LiveStockType, LiveStockTypeForm, 'livestock/livestock_type_form.html', 'data_management:livestock_type_detail', pk)

def livestock_type_delete(request, pk):
    return delete_object(request, LiveStockType, 'data_management:livestock_type_list', 'livestock/livestock_confirm_delete.html', pk)

# Feed
def feed_list(request):
    return list_objects(request, Feed, 'feed/feed_list.html')

def feed_create(request):
    return create_object(request, Feed, FeedForm, 'feed/feed_form.html', 'data_management:feed_list')

def feed_detail(request, pk):
    return detail_object(request, Feed, 'feed/feed_detail.html', pk)

def feed_update(request, pk):
    return update_object(request, Feed, FeedForm, 'feed/feed_form.html', 'data_management:feed_detail', pk)

def feed_delete(request, pk):
    return delete_object(request, Feed, 'data_management:feed_list', 'feed/feed_confirm_delete.html', pk)

# VaccinationRecord
def vaccinationrecord_list(request):
    return list_objects(request, VaccinationRecord, 'vaccinationrecord/vaccinationrecord_list.html')

def vaccinationrecord_create(request):
    return create_object(request, VaccinationRecord, VaccinationRecordForm, 'vaccinationrecord/vaccinationrecord_form.html', 'data_management:vaccinationrecord_list')

def vaccinationrecord_detail(request, pk):
    return detail_object(request, VaccinationRecord, 'vaccinationrecord/vaccinationrecord_detail.html', pk)

def vaccinationrecord_update(request, pk):
    return update_object(request, VaccinationRecord, VaccinationRecordForm, 'vaccinationrecord/vaccinationrecord_form.html', 'data_management:vaccinationrecord_detail', pk)

def vaccinationrecord_delete(request, pk):
    return delete_object(request, VaccinationRecord, 'data_management:vaccinationrecord_list', 'vaccinationrecord/vaccinationrecord_confirm_delete.html', pk)

# BreedingRecord
def breedingrecord_list(request):
    return list_objects(request, BreedingRecord, 'breedingrecord/breedingrecord_list.html')

def breedingrecord_create(request):
    return create_object(request, BreedingRecord, BreedingRecordForm, 'breedingrecord/breedingrecord_form.html', 'data_management:breedingrecord_list')

def breedingrecord_detail(request, pk):
    return detail_object(request, BreedingRecord, 'breedingrecord/breedingrecord_detail.html', pk)

def breedingrecord_update(request, pk):
    return update_object(request, BreedingRecord, BreedingRecordForm, 'breedingrecord/breedingrecord_form.html', 'data_management:breedingrecord_detail', pk)

def breedingrecord_delete(request, pk):
    return delete_object(request, BreedingRecord, 'data_management:breedingrecord_list', 'breedingrecord/breedingrecord_confirm_delete.html', pk)

# DeathRecord
def deathrecord_list(request):
    return list_objects(request, DeathRecord, 'deathrecord/deathrecord_list.html')

def deathrecord_create(request):
    return create_object(request, DeathRecord, DeathRecordForm, 'deathrecord/deathrecord_form.html', 'data_management:deathrecord_list')

def deathrecord_detail(request, pk):
    return detail_object(request, DeathRecord, 'deathrecord/deathrecord_detail.html', pk)

def deathrecord_update(request, pk):
    return update_object(request, DeathRecord, DeathRecordForm, 'deathrecord/deathrecord_form.html', 'data_management:deathrecord_detail', pk)

def deathrecord_delete(request, pk):
    return delete_object(request, DeathRecord, 'data_management:deathrecord_list', 'deathrecord/deathrecord_confirm_delete.html', pk)

# Event
def event_list(request):
    return list_objects(request, Event, 'event/event_list.html')

def event_create(request):
    return create_object(request, Event, EventForm, 'event/event_form.html', 'data_management:event_list')

def event_detail(request, pk):
    return detail_object(request, Event, 'event/event_detail.html', pk)

def event_update(request, pk):
    return update_object(request, Event, EventForm, 'event/event_form.html', 'data_management:event_detail', pk)

def event_delete(request, pk):
    return delete_object(request, Event, 'data_management:event_list', 'event/event_confirm_delete.html', pk)