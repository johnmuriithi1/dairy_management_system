from rest_framework import serializers
from .models import LiveStock, MilkProduction,Feed,HealthRecord

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStock
        fields = '__all__'


class MilkProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduction
        fields = '__all__'


class HealthRecordSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = HealthRecord  
        fields = '__all__'  

class FeedSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Feed  
        fields = '__all__'  
