from rest_framework import generics,filters  
from rest_framework.response import Response  
from rest_framework.permissions import AllowAny,IsAuthenticated  
from rest_framework_simplejwt.tokens import RefreshToken  
from django.contrib.auth import authenticate 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.models import User 
from .serializers import UserSerializer, FarmerSerializer, FarmAgentSerializer, VeterinaryPartnerSerializer
from django.contrib.auth import get_user_model
from .models import Farmer, FarmAgent, VeterinaryPartner
from django_filters.rest_framework import DjangoFilterBackend
from .permisions import IsFarmer,IsFarmAgent,IsVeterinaryPartner
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user
    Inherits from CreateAPIView to handle POST requests
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[AllowAny]

class LogInView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'acess':str(refresh.access_token),
            })
        return Response({'error':'Invalid credentials'})


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
     """  
    API view to retrieve, update, or delete the current user's profile.  
    Inherits from RetrieveUpdateDestroyAPIView for handling GET, PUT, and DELETE requests.  
    """
     queryset = User.objects.all()
     serializer_class = UserSerializer
     permission_classes = [IsAuthenticated]

     def get_object(self):
        """  
        Override to return the current authenticated user.  
        """
        user = self.request.user
        return user


class UserLogoutView():
    permmission_classes = [IsAuthenticated]

    def post(self,request):
        try: 
            # blacklist the refresh token
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist() # this will add the token to the blacklist

            return Response({"message":"Successfully Logged out."},status=205)
        except Exception as e:
            return Response({"error": str(e)},status=400)
# user management
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# Farmer Management  
class FarmerCreateView(generics.CreateAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer
    permission_classes = [IsFarmer]  

class FarmerListView(generics.ListAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer  
    permission_classes = [IsAuthenticated] 
    filters_backend = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['county','category']
    search_fields = ['name','farmer_code']


class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer  
    permission_classes = [IsAuthenticated] 


# Veterinary Partner Management  
class VeterinaryPartnerCreateView(generics.CreateAPIView):  
    queryset = VeterinaryPartner.objects.all()  
    serializer_class = VeterinaryPartnerSerializer
    permission_classes = [IsVeterinaryPartner ]

class VeterinaryPartnerListView(generics.ListAPIView):  
    queryset = VeterinaryPartner.objects.all()  
    serializer_class = VeterinaryPartnerSerializer  
    permission_classes = [IsAuthenticated]  
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  
    search_fields = ['name']  # Allow searching by name  

class VeterinaryPartnerDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = VeterinaryPartner  
    permission_classes = [IsAuthenticated] 


# Farm Agent Management 
class FarmAgentCreateView(generics.CreateAPIView):  
    queryset = FarmAgent.objects.all()  
    serializer_class = FarmAgentSerializer
    permission_classes = [IsFarmAgent]

class FarmAgentDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = FarmAgent.objects.all()  
    serializer_class = FarmAgentSerializer  
    permission_classes = [IsAuthenticated] 


# FarmAgent Management with Filtering and Search  
class FarmAgentListView(generics.ListAPIView):  
    queryset = FarmAgent.objects.all()  
    serializer_class = FarmAgentSerializer  
    permission_classes = [IsAuthenticated]  
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)  
    filterset_fields = ['county']  # Allow filtering by county  
    search_fields = ['full_name', 'agent_code']  # Allow searching by full_name and agent_code


def home(request):
    return render(request,'dairy_management_system/templates/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Inavlid Credentials')
    return render(request,'users/login.html')

def user_logout(request):
    logout(request)
    return render(request,'users/logout.html')

def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
    return render(request,'users/create_user.html')

def user_dashboard(request):
    return render(request,'users/dashboard.html')
