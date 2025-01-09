from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import (
    LivestockTypeForm,
    LivestockForm,
    AnimalProfileForm,
    MilkProductionForm,
    HealthRecordForm,
    FeedForm,
    VaccinationRecordForm,
    BreedingRecordForm,
    DeathRecordForm,
    EventForm
)
from .models import (
    LivestockType,
    Livestock,
    AnimalProfile,
    MilkProduction,
    HealthRecord,
    Feed,
    VaccinationRecord,
    BreedingRecord,
    DeathRecord,
    Event
)

# Livestock Type Views
class LivestockTypeListView(ListView):
    model = LivestockType
    template_name = 'livestock/livestock_type_list.html'
    context_object_name = 'livestock_types'

def create_livestock_type(request):
    if request.method == "POST":
        form = LivestockTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_management:livestock_type_list')
    else:
        form = LivestockTypeForm()
    
    return render(request, 'livestock/livestock_type_form.html', {'form': form})

def update_livestock_type(request, pk):
    livestock_type = get_object_or_404(LivestockType, pk=pk)
    
    if request.method == "POST":
        form = LivestockTypeForm(request.POST, instance=livestock_type)
        if form.is_valid():
            form.save()
            return redirect('data_management:livestock_type_list')
    else:
        form = LivestockTypeForm(instance=livestock_type)
    
    return render(request, 'livestock/livestock_type_form.html', {'form': form})

# Livestock Views
class LivestockListView(ListView):
    model = Livestock
    template_name = 'livestock/livestock_list.html'
    context_object_name = 'livestock_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Annotate each livestock with the count of related animal profiles
        for livestock in context['livestock_list']:
            livestock.animal_profile_count = AnimalProfile.objects.filter(livestock=livestock).count()
        return context

def create_livestock(request):
    if request.method == "POST":
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_management:livestock_list')
    else:
        form = LivestockForm()
    
    return render(request, 'livestock/livestock_form.html', {'form': form})

def update_livestock(request, pk):
    livestock = get_object_or_404(Livestock, pk=pk)
    
    if request.method == "POST":
        form = LivestockForm(request.POST, instance=livestock)
        if form.is_valid():
            form.save()
            return redirect('data_management:livestock_list')
    else:
        form = LivestockForm(instance=livestock)
    
    return render(request, 'livestock/livestock_form.html', {'form': form})

# Animal Profile Views
class AnimalProfileListView(ListView):
    model = AnimalProfile
    template_name = 'livestock/animal_profile_list.html'
    context_object_name = 'animal_profiles'

    def get_queryset(self):
        livestock_id = self.request.GET.get('livestock_id')
        if livestock_id:
            try:
                self.livestock = get_object_or_404(Livestock, pk=livestock_id)
                queryset = AnimalProfile.objects.filter(livestock=self.livestock)
                print(f"Queryset count for livestock {self.livestock.name}: {queryset.count()}")  # Debug print
                return queryset
            except ValueError:
                print("Invalid livestock_id")
                self.livestock = None
                return AnimalProfile.objects.none()
        else:
            self.livestock = None
            queryset = AnimalProfile.objects.all()
            print(f"Queryset count for all: {queryset.count()}")  # Debug print
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livestock'] = self.livestock
        return context

def create_animal_profile(request):
    """Creates a new AnimalProfile associated with a specific Livestock."""

    livestock_id = request.GET.get('livestock_id')

    if not livestock_id:
        # Handle the case where livestock_id is not provided
        return render(request, 'livestock/error.html', {'message': 'Livestock ID is required.'}) # Or redirect elsewhere

    try:
        livestock = Livestock.objects.get(pk=livestock_id)
    except Livestock.DoesNotExist:
         return render(request, 'livestock/error.html', {'message': 'Livestock not found.'})

    if request.method == "POST":
        form = AnimalProfileForm(request.POST, request.FILES)
        if form.is_valid():
            animal_profile = form.save(commit=False)
            animal_profile.livestock = livestock
            animal_profile.save()

            # Correct redirection using reverse and query parameters
            url = reverse('data_management:animal_profile_list')
            return HttpResponseRedirect(f'{url}?livestock_id={livestock.id}')
        else:
            # Re-render the form with errors if it's invalid
            return render(request, 'livestock/animal_profile_form.html', {'form': form, 'livestock': livestock})
    else:
        form = AnimalProfileForm()
    
    return render(request, 'livestock/animal_profile_form.html', {'form': form, 'livestock': livestock})

def update_animal_profile(request, pk):
    animal_profile = get_object_or_404(AnimalProfile, pk=pk)
    
    if request.method == "POST":
        form = AnimalProfileForm(request.POST, request.FILES, instance=animal_profile)
        if form.is_valid():
            form.save()
            return redirect('data_management:animal_profile_list')
    else:
        form = AnimalProfileForm(instance=animal_profile)
    
    return render(request, 'livestock/animal_profile_form.html', {'form': form})


def delete_animal_profile(request, pk):
    animal_profile = get_object_or_404(AnimalProfile, pk=pk)
    livestock_id = animal_profile.livestock.id  # Get the livestock ID before deleting
    if request.method == 'POST':
        animal_profile.delete()
        url = reverse('data_management:animal_profile_list')
        return HttpResponseRedirect(f'{url}?livestock_id={livestock_id}')
    return render(request, 'livestock/delete_animal_profile.html', {'animal_profile': animal_profile})



def view_animal_profile(request, pk):  # pk is important
    animal_profile = get_object_or_404(AnimalProfile, pk=pk)
    return render(request, 'livestock/view_animal_profile.html', {'animal_profile': animal_profile})


# Milk Production Views
class MilkProductionListView(ListView):
    model = MilkProduction
    template_name = 'milkproduction/milk_production_list.html'
    context_object_name = 'milk_production_records'
    ordering = ['-production_date'] #Order by date

    def get_queryset(self):
        animal_id = self.request.GET.get('animal_id')
        if animal_id:
            return MilkProduction.objects.filter(animal_id=animal_id)
        return MilkProduction.objects.all()

def create_milk_production(request):
    animal_id = request.GET.get('animal_id')
    if animal_id:
        animal = get_object_or_404(AnimalProfile, pk=animal_id)
    else:
        animal = None

    if request.method == 'POST':
        form = MilkProductionForm(request.POST)
        if form.is_valid():
            milk_production = form.save(commit=False)
            if animal:
                milk_production.animal = animal
            milk_production.save()
            if animal:
                url = reverse('data_management:milk_production_list')
                return HttpResponseRedirect(f'{url}?animal_id={animal.id}')
            else:
                return redirect('data_management:milk_production_list')
    else:
        if animal:
            form = MilkProductionForm(initial={'animal': animal})
        else:
            form = MilkProductionForm()
    return render(request, 'milkproduction/milk_production_form.html', {'form': form, 'animal': animal})

def update_milk_production(request, pk):
    milk_production = get_object_or_404(MilkProduction, pk=pk)
    if request.method == 'POST':
        form = MilkProductionForm(request.POST, instance=milk_production)
        if form.is_valid():
            milk_production = form.save()
            animal_id = milk_production.animal.id
            url = reverse('data_management:milk_production_list')
            return HttpResponseRedirect(f'{url}?animal_id={animal_id}')
    else:
        form = MilkProductionForm(instance=milk_production)
    return render(request, 'milkproduction/milk_production_form.html', {'form': form})

def delete_milk_production(request, pk):
    milk_production = get_object_or_404(MilkProduction, pk=pk)
    animal_id = milk_production.animal.id
    if request.method == 'POST':
        milk_production.delete()
        url = reverse('data_management:milk_production_list')
        return HttpResponseRedirect(f'{url}?animal_id={animal_id}')
    return render(request, 'milkproduction/delete_milk_production.html', {'milk_production': milk_production})

# Health Record Views
class HealthRecordListView(ListView):
    model = HealthRecord
    template_name = 'health_record_list.html'
    context_object_name = 'health_records'

def create_health_record(request):
   if request.method == "POST":
       # Implement the logic to create a health record
       pass  # Replace with actual implementation

def update_health_record(request, pk):
   health_record = get_object_or_404(HealthRecord, pk=pk)
   # Implement the logic to update a health record
   pass  # Replace with actual implementation

# Feed Views
class FeedListView(ListView):
   model = Feed
   template_name = 'feed_list.html'
   context_object_name = 'feed_records'

def create_feed(request):
   if request.method == "POST":
       # Implement the logic to create feed record
       pass  # Replace with actual implementation

def update_feed(request, pk):
   feed_item = get_object_or_404(Feed, pk=pk)
   # Implement the logic to update a feed record
   pass  # Replace with actual implementation

# Vaccination Record Views
class VaccinationRecordListView(ListView):
   model = VaccinationRecord
   template_name = 'vaccination_record_list.html'
   context_object_name = 'vaccination_records'

def create_vaccination_record(request):
   if request.method == "POST":
       # Implement the logic to create a vaccination record
       pass  # Replace with actual implementation

def update_vaccination_record(request, pk):
   vaccination_record = get_object_or_404(VaccinationRecord, pk=pk)
   # Implement the logic to update a vaccination record
   pass  # Replace with actual implementation

# Breeding Record Views
class BreedingRecordListView(ListView):
   model = BreedingRecord
   template_name = 'breeding_record_list.html'
   context_object_name = 'breeding_records'

def create_breeding_record(request):
   if request.method == "POST":
       # Implement the logic to create a breeding record
       pass  # Replace with actual implementation

def update_breeding_record(request, pk):
   breeding_record = get_object_or_404(BreedingRecord, pk=pk)
   # Implement the logic to update a breeding record
   pass  # Replace with actual implementation

# Death Record Views
class DeathRecordListView(ListView):
   model = DeathRecord
   template_name = 'death_record_list.html'
   context_object_name = 'death_records'

def create_death_record(request):
   if request.method == "POST":
       # Implement the logic to create a death record
       pass  # Replace with actual implementation

def update_death_record(request, pk):
   death_record = get_object_or_404(DeathRecord, pk=pk)
   # Implement the logic to update a death record
   pass  # Replace with actual implementation

# Event Views
class EventListView(ListView):
   model = Event
   template_name = 'event_list.html'
   context_object_name = 'events'

def create_event(request):
   if request.method == "POST":
       # Implement the logic to create an event record
       pass  # Replace with actual implementation

def update_event(request, pk):
   event_instance = get_object_or_404(Event, pk=pk)
   # Implement the logic to update an event record
   pass  # Replace with actual implementation

