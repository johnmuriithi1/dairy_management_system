from django.urls import path
from user_management.views import( RegisterView,UserDetailView,LogInView,
    UserCreateView, UserListView, FarmerCreateView, FarmerListView, FarmerDetailView,  
    FarmAgentCreateView, FarmAgentListView, FarmAgentDetailView,  
    VeterinaryPartnerCreateView, VeterinaryPartnerListView, VeterinaryPartnerDetailView
 )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'),
    # User URLs  
    path('users/', UserListView.as_view(), name='user-list'),  
    path('users/create/', UserCreateView.as_view(), name='user-create'),  
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), 

    # Farm Agent URLs  
    path('agents/', FarmAgentListView.as_view(), name='agent-list'),  
    path('agents/create/', FarmAgentCreateView.as_view(), name='agent-create'),  
    path('agents/<int:pk>/', FarmAgentDetailView.as_view(), name='agent-detail'),  

    # Veterinary Partner URLs  
    path('veterinary-partners/', VeterinaryPartnerListView.as_view(), name='vet-partner-list'),  
    path('veterinary-partners/create/', VeterinaryPartnerCreateView.as_view(), name='vet-partner-create'),  
    path('veterinary-partners/<int:pk>/', VeterinaryPartnerDetailView.as_view(), name='vet-partner-detail'),  
    
    path('profile/', UserDetailView.as_view(), name='profile'),
]