from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

def create_object(request, model_form, template_name, redirect_url):
    """
    Generic function to handle object creation.
    """
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model_form.Meta.model._meta.verbose_name} created successfully!')
            return redirect(redirect_url)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = model_form()
    return render(request, template_name, {'form': form})

# LivestockType Views
def livestock_type_list(request):
    livestock_types = LiveStockType.objects.all()
    return render(request, 'livestock/livestock_type_list.html', {'livestock_types': livestock_types})

def livestock_type_create(request):
    return create_object(request, LiveStockTypeForm, 'livestock/livestock_type_form.html', 'data_management:livestock_type_list')

def livestock_type_detail(request, pk):
    livestock_type = get_object_or_404(LiveStockType, pk=pk)
    return render(request, 'livestock/livestock_type_detail.html', {'livestock_type': livestock_type})

def livestock_type_edit(request, pk):
    livestock_type = get_object_or_404(LiveStockType, pk=pk)
    if request.method == 'POST':
        form = LiveStockTypeForm(request.POST, instance=livestock_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livestock Type updated successfully!')
            return redirect('data_management:livestock_type_detail', pk=livestock_type.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = LiveStockTypeForm(instance=livestock_type)
    return render(request, 'livestock/livestock_type_form.html', {'form': form, 'livestock_type': livestock_type})

def livestock_type_delete(request, pk):
    livestock_type = get_object_or_404(LiveStockType, pk=pk)
    if request.method == 'POST':
        livestock_type.delete()
        messages.success(request, "Livestock Type deleted successfully.")
        return redirect('data_management:livestock_type_list')
    return render(request, 'livestock/livestock_confirm_delete.html', {'livestock_type': livestock_type})

# Livestock Views
def livestock_list(request):
    livestock = LiveStock.objects.all()
    return render(request, 'livestock/livestock_list.html', {'livestock': livestock})

def livestock_create(request):
    return create_object(request, LiveStockForm, 'livestock/livestock_form.html', 'data_management:livestock_list')

def livestock_detail(request, pk):
    livestock = get_object_or_404(LiveStock, pk=pk)
    return render(request, 'livestock/livestock_detail.html', {'livestock': livestock})

def livestock_edit(request, pk):
    livestock = get_object_or_404(LiveStock, pk=pk)
    if request.method == 'POST':
        form = LiveStockForm(request.POST, request.FILES, instance=livestock)  # Include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Livestock updated successfully!')
            return redirect('data_management:livestock_detail', pk=livestock.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = LiveStockForm(instance=livestock)
    return render(request, 'livestock/livestock_form.html', {'form': form, 'livestock': livestock})

def livestock_delete(request, pk):
    livestock = get_object_or_404(LiveStock, pk=pk)
    if request.method == 'POST':
        livestock.delete()
        messages.success(request, "Livestock deleted successfully.")
        return redirect('data_management:livestock_list')
    return render(request, 'livestock/livestock_confirm_delete.html', {'livestock': livestock})

# Generic view for edit and delete
def edit_object(request, model, model_form, template_name, redirect_url, pk):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'{model._meta.verbose_name} updated successfully!')
            return redirect(redirect_url, pk=obj.pk)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = model_form(instance=obj)
    return render(request, template_name, {'form': form, model._meta.model_name: obj})

def delete_object(request, model, redirect_url, template_name, pk):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"{model._meta.verbose_name} deleted successfully.")
        return redirect(redirect_url)
    return render(request, template_name, {model._meta.model_name: obj})


# Other Model Views (using generic views)
def animalprofile_list(request):
    animalprofiles = AnimalProfile.objects.all()
    return render(request, 'animalprofile/animalprofile_list.html', {'animalprofiles': animalprofiles})

def animalprofile_create(request):
    return create_object(request, AnimalProfileForm, 'animalprofile/animalprofile_form.html', 'data_management:animalprofile_list')

def animalprofile_detail(request, pk):
    animalprofile = get_object_or_404(AnimalProfile, pk=pk)
    return render(request, 'animalprofile/animalprofile_detail.html', {'animalprofile': animalprofile})

def animalprofile_edit(request, pk):
    return edit_object(request, AnimalProfile, AnimalProfileForm, 'animalprofile/animalprofile_form.html', 'data_management:animalprofile_detail', pk)

def animalprofile_delete(request, pk):
    return delete_object(request, AnimalProfile, 'data_management:animalprofile_list', 'animalprofile/animalprofile_confirm_delete.html', pk)

# MilkProduction Views
def milkproduction_list(request):
    milkproductions = MilkProduction.objects.all()
    return render(request, 'milkproduction/milkproduction_list.html', {'milkproductions': milkproductions})

def milkproduction_create(request):
    return create_object(request, MilkProductionForm, 'milkproduction/milkproduction_form.html', 'data_management:milkproduction_list')

def milkproduction_detail(request, pk):
    milkproduction = get_object_or_404(MilkProduction, pk=pk)
    return render(request, 'milkproduction/milkproduction_detail.html', {'milkproduction': milkproduction})

def milkproduction_edit(request, pk):
    return edit_object(request, MilkProduction, MilkProductionForm, 'milkproduction/milkproduction_form.html', 'data_management:milkproduction_detail', pk)

def milkproduction_delete(request, pk):
    return delete_object(request, MilkProduction, 'data_management:milkproduction_list', 'milkproduction/milkproduction_confirm_delete.html', pk)

# HealthRecord Views
def healthrecord_list(request):
    healthrecords = HealthRecord.objects.all()
    return render(request, 'healthrecord/healthrecord_list.html', {'healthrecords': healthrecords})

def healthrecord_create(request):
    return create_object(request, HealthRecordForm, 'healthrecord/healthrecord_form.html', 'data_management:healthrecord_list')

def healthrecord_detail(request, pk):
    healthrecord = get_object_or_404(HealthRecord, pk=pk)
    return render(request, 'healthrecord/healthrecord_detail.html', {'healthrecord': healthrecord})

def healthrecord_edit(request, pk):
    return edit_object(request, HealthRecord, HealthRecordForm, 'healthrecord/healthrecord_form.html', 'data_management:healthrecord_detail', pk)

def healthrecord_delete(request, pk):
    return delete_object(request, HealthRecord, 'data_management:healthrecord_list', 'healthrecord/healthrecord_confirm_delete.html', pk)

# Feed Views
def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feed/feed_list.html', {'feeds': feeds})

def feed_create(request):
    return create_object(request, FeedForm, 'feed/feed_form.html', 'data_management:feed_list')

def feed_detail(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    return render(request, 'feed/feed_detail.html', {'feed': feed})

def feed_edit(request, pk):
    return edit_object(request, Feed, FeedForm, 'feed/feed_form.html', 'data_management:feed_detail', pk)

def feed_delete(request, pk):
    return delete_object(request, Feed, 'data_management:feed_list', 'feed/feed_confirm_delete.html', pk)

# VaccinationRecord Views
def vaccinationrecord_list(request):
    vaccinationrecords = VaccinationRecord.objects.all()
    return render(request, 'vaccinationrecord/vaccinationrecord_list.html', {'vaccinationrecords': vaccinationrecords})

def vaccinationrecord_create(request):
    return create_object(request, VaccinationRecordForm, 'vaccinationrecord/vaccinationrecord_form.html', 'data_management:vaccinationrecord_list')

def vaccinationrecord_detail(request, pk):
    vaccinationrecord = get_object_or_404(VaccinationRecord, pk=pk)
    return render(request, 'vaccinationrecord/vaccinationrecord_detail.html', {'vaccinationrecord': vaccinationrecord})

def vaccinationrecord_edit(request, pk):
    return edit_object(request, VaccinationRecord, VaccinationRecordForm, 'vaccinationrecord/vaccinationrecord_form.html', 'data_management:vaccinationrecord_detail', pk)

def vaccinationrecord_delete(request, pk):
    return delete_object(request, VaccinationRecord, 'data_management:vaccinationrecord_list', 'vaccinationrecord/vaccinationrecord_confirm_delete.html', pk)


# BreedingRecord Views
def breedingrecord_list(request):
    breedingrecords = BreedingRecord.objects.all()
    return render(request, 'breedingrecord/breedingrecord_list.html', {'breedingrecords': breedingrecords})

def breedingrecord_create(request):
    return create_object(request, BreedingRecordForm, 'breedingrecord/breedingrecord_form.html', 'data_management:breedingrecord_list')

def breedingrecord_detail(request, pk):
    breedingrecord = get_object_or_404(BreedingRecord, pk=pk)
    return render(request, 'breedingrecord/breedingrecord_detail.html', {'breedingrecord': breedingrecord})

def breedingrecord_edit(request, pk):
    return edit_object(request, BreedingRecord, BreedingRecordForm, 'breedingrecord/breedingrecord_form.html', 'data_management:breedingrecord_detail', pk)

def breedingrecord_delete(request, pk):
    return delete_object(request, BreedingRecord, 'data_management:breedingrecord_list', 'breedingrecord/breedingrecord_confirm_delete.html', pk)

# DeathRecord Views
def deathrecord_list(request):
    deathrecords = DeathRecord.objects.all()
    return render(request, 'deathrecord/deathrecord_list.html', {'deathrecords': deathrecords})

def deathrecord_create(request):
    return create_object(request, DeathRecordForm, 'deathrecord/deathrecord_form.html', 'data_management:deathrecord_list')

def deathrecord_detail(request, pk):
    deathrecord = get_object_or_404(DeathRecord, pk=pk)
    return render(request, 'deathrecord/deathrecord_detail.html', {'deathrecord': deathrecord})

def deathrecord_edit(request, pk):
    return edit_object(request, DeathRecord, DeathRecordForm, 'deathrecord/deathrecord_form.html', 'data_management:deathrecord_detail', pk)

def deathrecord_delete(request, pk):
    return delete_object(request, DeathRecord, 'data_management:deathrecord_list', 'deathrecord/deathrecord_confirm_delete.html', pk)

# Event Views
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})

def event_create(request):
    return create_object(request, EventForm, 'event/event_form.html', 'data_management:event_list')

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})

def event_edit(request, pk):
    return edit_object(request, Event, EventForm, 'event/event_form.html', 'data_management:event_detail', pk)

def event_delete(request, pk):
    return delete_object(request, Event, 'data_management:event_list', 'event/event_confirm_delete.html', pk)