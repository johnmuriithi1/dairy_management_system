from rest_framework import generics, filters,viewsets
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, FarmerSerializer, FarmAgentSerializer, VeterinaryPartnerSerializer
from .models import Farmer, FarmAgent, VeterinaryPartner, User
from django_filters.rest_framework import DjangoFilterBackend
from . permisions import IsFarmer, IsFarmAgent, IsVeterinaryPartner

# User Management

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# Registration and Login (already defined)

class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user
    Inherits from CreateAPIView to handle POST requests
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LogInView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'})


# User details (already defined)

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


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if refresh_token is None:
                return Response({"error": "Refresh token is required"}, status=400)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully Logged out."}, status=205)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

# Farmer Management (already defined)

class FarmerCreateView(generics.CreateAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer
    permission_classes = [IsFarmer]  

class FarmerListView(generics.ListAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer  
    permission_classes = [IsAuthenticated] 
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['county', 'category']
    search_fields = ['name', 'farmer_code']


class FarmerDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Farmer.objects.all()  
    serializer_class = FarmerSerializer  
    permission_classes = [IsAuthenticated] 


# Veterinary Partner Management (already defined)

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
    queryset = Farmer.objects.all()  # Update queryset to VeterinaryPartner.objects.all



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class FarmAgentViewSet(viewsets.ModelViewSet):
    queryset = FarmAgent.objects.all()
    serializer_class = FarmAgentSerializer

class VeterinaryPartnerViewSet(viewsets.ModelViewSet):
    queryset = VeterinaryPartner.objects.all()
    serializer_class = VeterinaryPartnerSerializer 