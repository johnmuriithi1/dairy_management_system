from django.contrib import admin
from .models import User, Farmer, FarmAgent, VeterinaryPartner, FarmWorker

# Register your models here.
admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(FarmAgent)
admin.site.register(VeterinaryPartner)
admin.site.register(FarmWorker)