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
    Event
)

class LivestockTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class LivestockAdmin(admin.ModelAdmin):
    list_display = ('name', 'farmer')
    search_fields = ('name',)

class AnimalProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'livestock', 'weight', 'date_of_birth')
    search_fields = ('name',)

class MilkProductionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'production_date', 'quantity_litres')
    search_fields = ('animal__name',)  # Use double underscore for related fields

class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'description')
    search_fields = ('animal__name',)

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')
    
class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ('animal', 'vaccine_name', 'date_given')
    
class BreedingRecordAdmin(admin.ModelAdmin):
    list_display = ('sire', 'dam', 'breeding_date')

class DeathRecordAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date_of_death', 'cause_of_death')

class EventAdmin(admin.ModelAdmin):
    list_display = ('animal', 'event_type', 'date')

# Register your models with custom admin classes
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
