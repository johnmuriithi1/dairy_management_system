from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
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
    template_name = "data_management/confirm_delete.html"
    success_url = None

# LIVESTOCK TYPE VIEWS
class LivestockTypeListView(GenericListView):
    model = LivestockType
    template_name = "livestock/livestock_list.html"

class LivestockTypeCreateView(GenericCreateView):
    model= LivestockType
    form_class = LivestockType


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
    context_object_name = "livestock_list"  # Updated to match template usage

class LivestockCreateView(GenericCreateView):
    model = Livestock
    form_class = LivestockForm
    template_name = "livestock/livestock_create.html"
    success_url = reverse_lazy("data_management:livestock_list")
    success_message = "Livestock '%(name)s' was successfully created."

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
class AnimalProfileListView(GenericListView):
    model = AnimalProfile
    template_name = "data_management/animal_profile_list.html"

class AnimalProfileCreateView(GenericCreateView):
    model = AnimalProfile
    form_class = AnimalProfileForm
    template_name = "data_management/animal_profile_form.html"
    success_url = reverse_lazy("data_management:animal_profile_list")
    success_message = "Animal Profile '%(name)s' was successfully created."

class AnimalProfileUpdateView(GenericUpdateView):
    model = AnimalProfile
    form_class = AnimalProfileForm
    template_name = "data_management/animal_profile_form.html"
    success_url = reverse_lazy("data_management:animal_profile_list")
    success_message = "Animal Profile '%(name)s' was successfully updated."

class AnimalProfileDeleteView(GenericDeleteView):
    model = AnimalProfile
    success_url = reverse_lazy("data_management:animal_profile_list")


# MILK PRODUCTION VIEWS
class MilkProductionListView(GenericListView):
    model = MilkProduction
    template_name = "data_management/milk_production_list.html"

class MilkProductionCreateView(GenericCreateView):
    model = MilkProduction
    form_class = MilkProductionForm
    template_name = "data_management/milk_production_form.html"
    success_url = reverse_lazy("data_management:milk_production_list")
    success_message = "Milk Production Record was successfully created."

class MilkProductionUpdateView(GenericUpdateView):
    model = MilkProduction
    form_class = MilkProductionForm
    template_name = "data_management/milk_production_form.html"
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
