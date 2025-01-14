from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import (
    LivestockType, Livestock, AnimalProfile, MilkProduction, HealthRecord,
    Feed, VaccinationRecord, BreedingRecord, DeathRecord, Event
)
from .forms import (
    LivestockTypeForm, LivestockForm, AnimalProfileForm, MilkProductionForm,
    HealthRecordForm, FeedForm, VaccinationRecordForm, BreedingRecordForm,
    DeathRecordForm, EventForm
)

# Generic SuccessMessageMixin for all create/update views
class SuccessMessageView(SuccessMessageMixin):
    success_message = "%(name)s was successfully %(action)s."

# Base CRUD Views
class GenericListView(ListView):
    model = None
    template_name = None
    context_object_name = "objects"

class GenericCreateView(SuccessMessageView, CreateView):
    model = None
    form_class = None
    template_name = None
    success_url = None
    success_message = "%(name)s was successfully created."

class GenericUpdateView(SuccessMessageView, UpdateView):
    model = None
    form_class = None
    template_name = None
    success_url = None
    success_message = "%(name)s was successfully updated."

class GenericDeleteView(DeleteView):
    model = None
    template_name = "livestock/confirm_delete.html"
    success_url = None

# LIVESTOCK TYPE VIEWS
class LivestockTypeListView(ListView):
    model = LivestockType
    template_name = "livestock/livestock_type_list.html"
    context_object_name = "livestock_types"

    def get_queryset(self):
        return LivestockType.objects.prefetch_related("livestocks")

class LivestockTypeCreateView(GenericCreateView):
    model = LivestockType
    form_class = LivestockTypeForm  
    template_name = "livestock/livestock_type_create.html"  
    success_url = reverse_lazy("data_management:livestock_type_list")  # Redirect after successful creation
    success_message = "Livestock Type '%(name)s' was successfully created."


class LivestockTypeUpdateView(GenericUpdateView):
    model = LivestockType
    form_class = LivestockTypeForm
    template_name = "data_management/livestock_type_form.html"
    success_url = reverse_lazy("data_management:livestock_type_list")
    success_message = "Livestock Type '%(name)s' was successfully updated."

class LivestockTypeDeleteView(GenericDeleteView):
    model = LivestockType
    success_url = reverse_lazy("data_management:livestock_type_list")


# LIVESTOCK VIEWS
class LivestockListView(GenericListView):
    model = Livestock
    template_name = "livestock/livestock_list.html"
    context_object_name = "livestock_list"  # To match template usage

    def get_queryset(self):
        queryset = super().get_queryset()
        livestock_type_id = self.request.GET.get("livestock_type")
        if livestock_type_id:
            queryset = queryset.filter(livestock_type_id=livestock_type_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livestock_type_id = self.request.GET.get("livestock_type")
        if livestock_type_id:
            context["livestock_type"] = LivestockType.objects.filter(pk=livestock_type_id).first()
        return context

class LivestockCreateView(GenericCreateView):
    model = Livestock
    form_class = LivestockForm
    template_name = "livestock/livestock_create.html"
    success_url = reverse_lazy("data_management:livestock_list")
    success_message = "Livestock '%(name)s' was successfully created."

    def get_initial(self):
        initial = super().get_initial()
        livestock_type_id = self.request.GET.get('livestock_type')
        if livestock_type_id:
            initial['livestock_type'] = LivestockType.objects.filter(pk=livestock_type_id).first()
        return initial

class LivestockUpdateView(GenericUpdateView):
    model = Livestock
    form_class = LivestockForm
    template_name = "livestock/livestock_update.html"
    success_url = reverse_lazy("data_management:livestock_list")
    success_message = "Livestock '%(name)s' was successfully updated."

class LivestockDeleteView(GenericDeleteView):
    model = Livestock
    template_name = "livestock/confirm_delete.html"
    success_url = reverse_lazy("data_management:livestock_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["livestock"] = self.object  # Pass object as 'livestock'
        return context


# ANIMAL PROFILE VIEWS
class AnimalProfileListView(ListView):
    model = AnimalProfile
    template_name = "livestock/animal_profile_list.html"
    context_object_name = "animal_profiles"

    def get_queryset(self):
        queryset = super().get_queryset()
        livestock_id = self.request.GET.get('livestock')
        if livestock_id:
            queryset = queryset.filter(livestock__id=livestock_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livestock_id = self.request.GET.get('livestock')
        if livestock_id:
            context['livestock'] = get_object_or_404(Livestock, id=livestock_id)
        return context

class AnimalProfileCreateView(CreateView):
    model = AnimalProfile
    form_class = AnimalProfileForm
    template_name = "livestock/animal_profile_form.html"

    def get_initial(self):
        """Prepopulate the livestock field if livestock ID is passed in the query."""
        initial = super().get_initial()
        livestock_id = self.request.GET.get("livestock")
        if livestock_id:
            livestock = get_object_or_404(Livestock, id=livestock_id)
            initial["livestock"] = livestock
        return initial

    def get_context_data(self, **kwargs):
        """Pass the livestock object to the template for cancel link."""
        context = super().get_context_data(**kwargs)
        livestock_id = self.request.GET.get("livestock")
        if livestock_id:
            context["livestock"] = get_object_or_404(Livestock, id=livestock_id)
        return context

    def get_success_url(self):
        """Redirect to the animal profile list for the selected livestock."""
        livestock_id = self.request.GET.get("livestock")
        if livestock_id:
            return reverse("data_management:animal_profile_list") + f"?livestock={livestock_id}"
        return reverse("data_management:animal_profile_list")

    
    

class AnimalProfileUpdateView(GenericUpdateView):
    model = AnimalProfile
    form_class = AnimalProfileForm
    template_name = "livestock/animal_profile_form.html"
    success_url = reverse_lazy("data_management:animal_profile_list")
    success_message = "Animal Profile '%(name)s' was successfully updated."


class AnimalProfileDetailView(DetailView):
    model = AnimalProfile
    template_name = "livestock/view_animal_profile.html"
    context_object_name = "animal_profile"


class AnimalProfileDeleteView(GenericDeleteView):
    model = AnimalProfile
    template_name = "livestock/confirm_delete.html"
    success_url = reverse_lazy("data_management:animal_profile_list")
    success_message = "Animal Profile was successfully deleted."


# MILK PRODUCTION VIEWS
class MilkProductionListView(ListView):
    model = MilkProduction
    template_name = "milkproduction/milk_production_list.html"
    context_object_name = "milk_production_records"

    def get_queryset(self):
        queryset = super().get_queryset()
        animal_id = self.request.GET.get("animal_id")
        if animal_id:
            queryset = queryset.filter(animal_profile__id=animal_id)
        return queryset


class MilkProductionCreateView(CreateView):
    model = MilkProduction
    form_class = MilkProductionForm
    template_name = "milkproduction/milk_production_form.html"
    success_url = reverse_lazy("data_management:milk_production_list")

    def get_initial(self):
        initial = super().get_initial()
        # Get the animal_profile_id from the query parameters
        animal_profile_id = self.request.GET.get("animal_profile")
        if animal_profile_id:
            # Fetch the AnimalProfile instance
            animal_profile = get_object_or_404(AnimalProfile, pk=animal_profile_id)
            initial["animal_profile"] = animal_profile
            # Ensure livestock is set based on the selected animal profile
            initial["livestock"] = animal_profile.livestock  # Set livestock field from AnimalProfile

        return initial

    def form_valid(self, form):
        # Set livestock explicitly if it's not already set
        if not form.instance.livestock:
            animal_profile = form.instance.animal_profile
            form.instance.livestock = animal_profile.livestock  # Set livestock from the animal profile

        return super().form_valid(form)



class MilkProductionUpdateView(GenericUpdateView):
    model = MilkProduction
    form_class = MilkProductionForm
    template_name = "milkproduction/milk_production_form.html"
    success_url = reverse_lazy("data_management:milk_production_list")
    success_message = "Milk Production Record was successfully updated."

class MilkProductionDeleteView(GenericDeleteView):
    model = MilkProduction
    success_url = reverse_lazy("data_management:milk_production_list")


# HEALTH RECORD VIEWS
class HealthRecordListView(GenericListView):
    model = HealthRecord
    template_name = "data_management/health_record_list.html"

class HealthRecordCreateView(GenericCreateView):
    model = HealthRecord
    form_class = HealthRecordForm
    template_name = "data_management/health_record_form.html"
    success_url = reverse_lazy("data_management:health_record_list")
    success_message = "Health Record was successfully created."

class HealthRecordUpdateView(GenericUpdateView):
    model = HealthRecord
    form_class = HealthRecordForm
    template_name = "data_management/health_record_form.html"
    success_url = reverse_lazy("data_management:health_record_list")
    success_message = "Health Record was successfully updated."

class HealthRecordDeleteView(GenericDeleteView):
    model = HealthRecord
    success_url = reverse_lazy("data_management:health_record_list")


# FEED VIEWS
class FeedListView(GenericListView):
    model = Feed
    template_name = "data_management/feed_list.html"

class FeedCreateView(GenericCreateView):
    model = Feed
    form_class = FeedForm
    template_name = "data_management/feed_form.html"
    success_url = reverse_lazy("data_management:feed_list")
    success_message = "Feed Record was successfully created."

class FeedUpdateView(GenericUpdateView):
    model = Feed
    form_class = FeedForm
    template_name = "data_management/feed_form.html"
    success_url = reverse_lazy("data_management:feed_list")
    success_message = "Feed Record was successfully updated."

class FeedDeleteView(GenericDeleteView):
    model = Feed
    success_url = reverse_lazy("data_management:feed_list")


# VACCINATION RECORD VIEWS
class VaccinationRecordListView(GenericListView):
    model = VaccinationRecord
    template_name = "data_management/vaccination_record_list.html"

class VaccinationRecordCreateView(GenericCreateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = "data_management/vaccination_record_form.html"
    success_url = reverse_lazy("data_management:vaccination_record_list")
    success_message = "Vaccination Record was successfully created."

class VaccinationRecordUpdateView(GenericUpdateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = "data_management/vaccination_record_form.html"
    success_url = reverse_lazy("data_management:vaccination_record_list")
    success_message = "Vaccination Record was successfully updated."

class VaccinationRecordDeleteView(GenericDeleteView):
    model = VaccinationRecord
    success_url = reverse_lazy("data_management:vaccination_record_list")


# BREEDING RECORD VIEWS
class BreedingRecordListView(GenericListView):
    model = BreedingRecord
    template_name = "data_management/breeding_record_list.html"

class BreedingRecordCreateView(GenericCreateView):
    model = BreedingRecord
    form_class = BreedingRecordForm
    template_name = "data_management/breeding_record_form.html"
    success_url = reverse_lazy("data_management:breeding_record_list")
    success_message = "Breeding Record was successfully created."

class BreedingRecordUpdateView(GenericUpdateView):
    model = BreedingRecord
    form_class = BreedingRecordForm
    template_name = "data_management/breeding_record_form.html"
    success_url = reverse_lazy("data_management:breeding_record_list")
    success_message = "Breeding Record was successfully updated."

class BreedingRecordDeleteView(GenericDeleteView):
    model = BreedingRecord
    success_url = reverse_lazy("data_management:breeding_record_list")


# DEATH RECORD VIEWS
class DeathRecordListView(GenericListView):
    model = DeathRecord
    template_name = "data_management/death_record_list.html"

class DeathRecordCreateView(GenericCreateView):
    model = DeathRecord
    form_class = DeathRecordForm
    template_name = "data_management/death_record_form.html"
    success_url = reverse_lazy("data_management:death_record_list")
    success_message = "Death Record was successfully created."

class DeathRecordUpdateView(GenericUpdateView):
    model = DeathRecord
    form_class = DeathRecordForm
    template_name = "data_management/death_record_form.html"
    success_url = reverse_lazy("data_management:death_record_list")
    success_message = "Death Record was successfully updated."

class DeathRecordDeleteView(GenericDeleteView):
    model = DeathRecord
    success_url = reverse_lazy("data_management:death_record_list")


# EVENT VIEWS
class EventListView(GenericListView):
    model = Event
    template_name = "data_management/event_list.html"

class EventCreateView(GenericCreateView):
    model = Event
    form_class = EventForm
    template_name = "data_management/event_form.html"
    success_url = reverse_lazy("data_management:event_list")
    success_message = "Event '%(title)s' was successfully created."

class EventUpdateView(GenericUpdateView):
    model = Event
    form_class = EventForm
    template_name = "data_management/event_form.html"
    success_url = reverse_lazy("data_management:event_list")
    success_message = "Event '%(title)s' was successfully updated."

class EventDeleteView(GenericDeleteView):
    model = Event
    success_url = reverse_lazy("data_management:event_list")
