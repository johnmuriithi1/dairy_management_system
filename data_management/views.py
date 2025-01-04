from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import LiveStock, AnimalProfile, MilkProduction, HealthRecord, Feed
from .forms import LiveStockForm, AnimalProfileForm, MilkProductionForm, HealthRecordForm, FeedForm

def create_object(request, model_form, template_name, redirect_url):
    if request.method == 'POST':
        form = model_form(request.POST, request.FILES)  # Handle file uploads
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

def livestock_type_list(request):
    livestock_types = list(LiveStock.objects.values_list('animal_type', flat=True).distinct()) # Convert to list here
    print(livestock_types)  # Print the list (now a Python list)
    return render(request, 'livestock/livestock_type_list.html', {'livestock_types': livestock_types})

def livestock_list(request, animal_type):
    """Displays livestock of a specific type."""
    livestock = LiveStock.objects.filter(animal_type=animal_type)
    return render(request, 'livestock/livestock_list.html', {'livestock': livestock, 'animal_type': animal_type})


def livestock_create(request):
    return create_object(request, LiveStockForm, 'livestock/livestock_form.html', 'data_management:livestock_list')  # Using namespace

def livestock_detail(request, pk):
    livestock = LiveStock.objects.get(pk=pk)
    return render(request, 'livestock/livestock_detail.html', {'livestock': livestock})

def animalprofile_list(request):
    animalprofiles = AnimalProfile.objects.all()
    return render(request, 'animalprofile/animalprofile_list.html', {'animalprofiles': animalprofiles})

def animalprofile_create(request):
    return create_object(request, AnimalProfileForm, 'animalprofile/animalprofile_form.html', 'animalprofile_list')

def animalprofile_detail(request, pk):
    animalprofile = AnimalProfile.objects.get(pk=pk)
    return render(request, 'animalprofile/animalprofile_detail.html', {'animalprofile': animalprofile})

def milkproduction_list(request):
    milkproductions = MilkProduction.objects.all()
    return render(request, 'milkproduction/milkproduction_list.html', {'milkproductions': milkproductions})

def milkproduction_create(request):
    return create_object(request, MilkProductionForm, 'milkproduction/milkproduction_form.html', 'milkproduction_list')

def milkproduction_detail(request, pk):
    milkproduction = MilkProduction.objects.get(pk=pk)
    return render(request, 'milkproduction/milkproduction_detail.html', {'milkproduction': milkproduction})

def healthrecord_list(request):
    healthrecords = HealthRecord.objects.all()
    return render(request, 'healthrecord/healthrecord_list.html', {'healthrecords': healthrecords})

def healthrecord_create(request):
    return create_object(request, HealthRecordForm, 'healthrecord/healthrecord_form.html', 'healthrecord_list')

def healthrecord_detail(request, pk):
    healthrecord = HealthRecord.objects.get(pk=pk)
    return render(request, 'healthrecord/healthrecord_detail.html', {'healthrecord': healthrecord})

def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feed/feed_list.html', {'feeds': feeds})

def feed_create(request):
    return create_object(request, FeedForm, 'feed/feed_form.html', 'feed_list')


def livestock_edit(request, pk):
    livestock = get_object_or_404(LiveStock, pk=pk) # Get the livestock or return a 404 error
    if request.method == 'POST':
        form = LiveStockForm(request.POST, request.FILES, instance=livestock) # instance to update existing object
        if form.is_valid():
            form.save()
            messages.success(request, 'Livestock updated successfully!')
            return redirect('data_management:livestock_detail', pk=livestock.pk) # Redirect to detail view after edit
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = LiveStockForm(instance=livestock) # Populate form with existing data
    return render(request, 'livestock/livestock_form.html', {'form': form, 'livestock': livestock}) # Pass livestock to context

def livestock_delete(request, pk):
    livestock = get_object_or_404(LiveStock, pk=pk)
    if request.method == 'POST':
        livestock.delete()
        messages.success(request, "Livestock deleted successfully.")
        return redirect('data_management:livestock_list')
    return render(request, 'livestock/livestock_confirm_delete.html', {'livestock': livestock})