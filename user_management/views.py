from rest_framework import generics  
from rest_framework.response import Response  
from rest_framework.permissions import AllowAny  
from rest_framework_simplejwt.tokens import RefreshToken  
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User 
from .serializers import UserSerializer 


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

     def get_object(self):
        """  
        Override to return the current authenticated user.  
        """
        user = self.request.user
        return user
