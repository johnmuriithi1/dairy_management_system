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
class HealthRecordListView(ListView):
    model = HealthRecord
    template_name = "data_management/health_record_list.html"
    context_object_name = "health_records"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return HealthRecord.objects.filter(animal_profile__id=animal_profile_id)
        return HealthRecord.objects.all()

class HealthRecordCreateView(CreateView):
    model = HealthRecord
    form_class = HealthRecordForm
    template_name = "data_management/health_record_form.html"

    def get_initial(self):
        initial = super().get_initial()
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            animal_profile = get_object_or_404(AnimalProfile, id=animal_profile_id)
            initial['animal_profile'] = animal_profile
        return initial

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:health_record_list") + f"?animal_profile={animal_profile_id}"

class HealthRecordUpdateView(UpdateView):
    model = HealthRecord
    form_class = HealthRecordForm
    template_name = "data_management/health_record_form.html"

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:health_record_list") + f"?animal_profile={animal_profile_id}"

class HealthRecordDeleteView(DeleteView):
    model = HealthRecord
    success_url = reverse_lazy("data_management:health_record_list")


# FEED VIEWS
class FeedListView(ListView):
    model = Feed
    template_name = "data_management/feed_list.html"
    context_object_name = "feed_records"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return Feed.objects.filter(animal_profile__id=animal_profile_id)
        return Feed.objects.all()

class FeedCreateView(CreateView):
    model = Feed
    form_class = FeedForm
    template_name = "data_management/feed_form.html"

    def get_initial(self):
        initial = super().get_initial()
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            animal_profile = get_object_or_404(AnimalProfile, id=animal_profile_id)
            initial['animal_profile'] = animal_profile
        return initial

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:feed_list") + f"?animal_profile={animal_profile_id}"

class FeedUpdateView(UpdateView):
    model = Feed
    form_class = FeedForm
    template_name = "data_management/feed_form.html"

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:feed_list") + f"?animal_profile={animal_profile_id}"

class FeedDeleteView(DeleteView):
    model = Feed
    success_url = reverse_lazy("data_management:feed_list")


# VACCINATION RECORD VIEWS
class VaccinationRecordListView(ListView):
    model = VaccinationRecord
    template_name = "data_management/vaccination_record_list.html"
    context_object_name = "vaccination_records"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return VaccinationRecord.objects.filter(animal_profile__id=animal_profile_id)
        return VaccinationRecord.objects.all()

class VaccinationRecordCreateView(CreateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = "data_management/vaccination_record_form.html"

    def get_initial(self):
        initial = super().get_initial()
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            animal_profile = get_object_or_404(AnimalProfile, id=animal_profile_id)
            initial['animal_profile'] = animal_profile
        return initial

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:vaccination_record_list") + f"?animal_profile={animal_profile_id}"

class VaccinationRecordUpdateView(UpdateView):
    model = VaccinationRecord
    form_class = VaccinationRecordForm
    template_name = "data_management/vaccination_record_form.html"

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:vaccination_record_list") + f"?animal_profile={animal_profile_id}"

class VaccinationRecordDeleteView(DeleteView):
    model = VaccinationRecord
    success_url = reverse_lazy("data_management:vaccination_record_list")


# BREEDING RECORD VIEWS
class BreedingRecordListView(ListView):
    model = BreedingRecord
    template_name = "data_management/breeding_record_list.html"
    context_object_name = "breeding_records"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return BreedingRecord.objects.filter(animal_profile__id=animal_profile_id)
        return BreedingRecord.objects.all()

class BreedingRecordCreateView(CreateView):
    model = BreedingRecord
    form_class = BreedingRecordForm
    template_name = "data_management/breeding_record_form.html"

    def form_valid(self, form):
        # Handle new animal birth
        response = super().form_valid(form)
        
        # If the breeding record involves the birth of a new animal
        if form.instance.is_birthing:
            # Create a new animal profile (new born animal)
            new_animal_profile = AnimalProfile.objects.create(
                livestock=form.instance.livestock,
                birth_date=form.instance.date_of_birth,
                name=form.instance.newborn_name,
                # Other necessary fields here...
            )
            # Optionally link the new animal profile to any other related data
        return response

    def get_success_url(self):
        return reverse_lazy("data_management:breeding_record_list")

class BreedingRecordUpdateView(UpdateView):
    model = BreedingRecord
    form_class = BreedingRecordForm
    template_name = "data_management/breeding_record_form.html"

    def get_success_url(self):
        return reverse_lazy("data_management:breeding_record_list")

class BreedingRecordDeleteView(DeleteView):
    model = BreedingRecord
    success_url = reverse_lazy("data_management:breeding_record_list")


# DEATH RECORD VIEWS
class DeathRecordListView(ListView):
    model = DeathRecord
    template_name = "data_management/death_record_list.html"
    context_object_name = "death_records"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return DeathRecord.objects.filter(animal_profile__id=animal_profile_id)
        return DeathRecord.objects.all()

class DeathRecordCreateView(CreateView):
    model = DeathRecord
    form_class = DeathRecordForm
    template_name = "data_management/death_record_form.html"

    def get_initial(self):
        initial = super().get_initial()
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            animal_profile = get_object_or_404(AnimalProfile, id=animal_profile_id)
            initial['animal_profile'] = animal_profile
        return initial

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:death_record_list") + f"?animal_profile={animal_profile_id}"

class DeathRecordUpdateView(UpdateView):
    model = DeathRecord
    form_class = DeathRecordForm
    template_name = "data_management/death_record_form.html"

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:death_record_list") + f"?animal_profile={animal_profile_id}"

class DeathRecordDeleteView(DeleteView):
    model = DeathRecord
    success_url = reverse_lazy("data_management:death_record_list")


# EVENT VIEWS
class EventListView(ListView):
    model = Event
    template_name = "data_management/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            return Event.objects.filter(animal_profile__id=animal_profile_id)
        return Event.objects.all()

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "data_management/event_form.html"

    def get_initial(self):
        initial = super().get_initial()
        animal_profile_id = self.request.GET.get('animal_profile')
        if animal_profile_id:
            animal_profile = get_object_or_404(AnimalProfile, id=animal_profile_id)
            initial['animal_profile'] = animal_profile
        return initial

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:event_list") + f"?animal_profile={animal_profile_id}"

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "data_management/event_form.html"

    def get_success_url(self):
        animal_profile_id = self.object.animal_profile.id
        return reverse("data_management:event_list") + f"?animal_profile={animal_profile_id}"

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy("data_management:event_list")
