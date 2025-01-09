from django.contrib import admin
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
    Event,
)

# LivestockType Admin
class LivestockTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


# Livestock Admin
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'livestock_type', 'date_of_birth', 'gender', 'unique_id')
    list_filter = ('livestock_type', 'gender')
    search_fields = ('name', 'unique_id')


# AnimalProfile Admin
class AnimalProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'health_status', 'weight', 'birth_weight', 'notes')
    list_filter = ('health_status',)
    search_fields = ('livestock__name', 'health_status')


# MilkProduction Admin
class MilkProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'date', 'quantity')
    list_filter = ('date',)
    search_fields = ('livestock__name',)


# HealthRecord Admin
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'date', 'issue', 'treatment', 'veterinarian')
    list_filter = ('date',)
    search_fields = ('livestock__name', 'issue', 'veterinarian')


# Feed Admin
class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'date', 'feed_type', 'quantity')
    list_filter = ('date', 'feed_type')
    search_fields = ('livestock__name', 'feed_type')


# VaccinationRecord Admin
class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'vaccine_name', 'date_administered', 'next_due_date')
    list_filter = ('date_administered', 'vaccine_name')
    search_fields = ('livestock__name', 'vaccine_name')


# BreedingRecord Admin
class BreedingRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'mating_date', 'expected_due_date', 'outcome')
    list_filter = ('mating_date', 'outcome')
    search_fields = ('livestock__name',)


# DeathRecord Admin
class DeathRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'date', 'cause')
    search_fields = ('livestock__name', 'cause')


# Event Admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'livestock', 'date', 'event_type', 'description')
    list_filter = ('date', 'event_type')
    search_fields = ('livestock__name', 'event_type', 'description')


# Registering all models
admin.site.register(LivestockType, LivestockTypeAdmin)
admin.site.register(Livestock, LivestockAdmin)
admin.site.register(AnimalProfile, AnimalProfileAdmin)
admin.site.register(MilkProduction, MilkProductionAdmin)
admin.site.register(HealthRecord, HealthRecordAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(VaccinationRecord, VaccinationRecordAdmin)
admin.site.register(BreedingRecord, BreedingRecordAdmin)
admin.site.register(DeathRecord, DeathRecordAdmin)
admin.site.register(Event, EventAdmin)
