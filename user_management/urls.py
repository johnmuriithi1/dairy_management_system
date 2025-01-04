from django.urls import path
from .normal_views import (
    home,
    user_login,
    user_logout,
    create_user,
    user_dashboard,
    edit_profile,
    complete_farm_agent_profile,
    complete_veterinary_partner_profile,
    complete_farmer_profile,
    profile,
)
app_name = 'user_management'


urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('create_user/', create_user, name='create_user'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('profile_edit/', edit_profile, name='profile_edit'),
    path('complete_farm_agent_profile/', complete_farm_agent_profile, name='complete_farm_agent_profile'),
    path('complete_veterinary_partner_profile/', complete_veterinary_partner_profile, name='complete_veterinary_partner_profile'),
    path('complete_farmer_profile/', complete_farmer_profile, name='complete_farmer_profile'),
]