from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserCReationForm 
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = UserCReationForm
    form = UserCReationForm
    model = User
    list_display =['email','username']

admin.site.register(User,CustomUserAdmin)




