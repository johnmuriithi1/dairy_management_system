from django.urls import path
from . import api_views  # Import from api_views.py

app_name = 'user_management'

urlpatterns = [
    # User Management
    path('users/', api_views.UserListView.as_view(), name='user-list'),
    path('users/create/', api_views.UserCreateView.as_view(), name='user-create'),

    # Registration and Login
    path('register/', api_views.RegisterView.as_view(), name='register'),
    path('login/', api_views.LogInView.as_view(), name='login'),
    path('logout/', api_views.UserLogoutView.as_view(), name='logout'),

    # User Details (Profile)
    path('profile/', api_views.UserDetailView.as_view(), name='profile'),

    # Farmer Management
    path('farmers/', api_views.FarmerListView.as_view(), name='farmer-list'),
    path('farmers/create/', api_views.FarmerCreateView.as_view(), name='farmer-create'),
    path('farmers/<int:pk>/', api_views.FarmerDetailView.as_view(), name='farmer-detail'),

    # Veterinary Partner Management
    path('veterinarypartners/', api_views.VeterinaryPartnerListView.as_view(), name='veterinarypartner-list'),
    path('veterinarypartners/create/', api_views.VeterinaryPartnerCreateView.as_view(), name='veterinarypartner-create'),
    path('veterinarypartners/<int:pk>/', api_views.VeterinaryPartnerDetailView.as_view(), name='veterinarypartner-detail'),
]