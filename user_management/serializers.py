from rest_framework import serializers  
from django.contrib.auth import get_user_model 
from .models import Farmer,FarmAgent,VeterinaryPartner 

User = get_user_model()  

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']  
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):  
        user = User(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        return user 

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class FarmAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmAgent
        fields = '__all__'

class VeterinaryPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryPartner
        fields = '__all__'