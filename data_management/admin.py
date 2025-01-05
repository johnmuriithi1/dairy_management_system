from django.contrib import admin
from .models import LiveStockType, LiveStock, AnimalProfile, MilkProduction, HealthRecord, Feed

admin.site.register(LiveStockType)
admin.site.register(LiveStock)
admin.site.register(AnimalProfile)
admin.site.register(MilkProduction)
admin.site.register(HealthRecord)
admin.site.register(Feed)