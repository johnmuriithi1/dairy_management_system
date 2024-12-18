from django.urls import path
from user_management.views import( RegisterView,UserDetailView,LogInView,
    UserCreateView, UserListView, FarmerCreateView, FarmerListView, FarmerDetailView,
    FarmAgentCreateView, FarmAgentListView, FarmAgentDetailView,  
    VeterinaryPartnerCreateView, VeterinaryPartnerListView, VeterinaryPartnerDetailView,user_dashboard,user_login,create_user,user_logout,home)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LogInView.as_view(), name='login'),
    # User URLs  
    path('api/users/', UserListView.as_view(), name='user-list'),  
    path('api/users/create/', UserCreateView.as_view(), name='user-create'),  
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), 

    # Farm Agent URLs  
    path('api/agents/', FarmAgentListView.as_view(), name='agent-list'),  
    path('api/agents/create/', FarmAgentCreateView.as_view(), name='agent-create'),  
    path('api/agents/<int:pk>/', FarmAgentDetailView.as_view(), name='agent-detail'),  

    # Veterinary Partner URLs  
    path('api/veterinary-partners/', VeterinaryPartnerListView.as_view(), name='vet-partner-list'),  
    path('api/veterinary-partners/create/', VeterinaryPartnerCreateView.as_view(), name='vet-partner-create'),  
    path('api/veterinary-partners/<int:pk>/', VeterinaryPartnerDetailView.as_view(), name='vet-partner-detail'),  
    
    path('api/profile/', UserDetailView.as_view(), name='profile'),
    
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_user/', create_user, name='create_user'),
    path('dashboard/', user_dashboard, name='dashboard'),
]