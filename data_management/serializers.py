from rest_framework import serializers
from .models import (
    LiveStockType, LiveStock, AnimalProfile, MilkProduction,
    HealthRecord, Feed, VaccinationRecord, BreedingRecord,
    DeathRecord, Event
)

class LiveStockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStockType
        fields = '__all__'

class LiveStockSerializer(serializers.ModelSerializer):
    livestock_type = LiveStockTypeSerializer()
    class Meta:
        model = LiveStock
        fields = '__all__'

class AnimalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalProfile
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

class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'

class BreedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedingRecord
        fields = '__all__'

class DeathRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeathRecord
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


# Serializers with Nested Relationships (for more detailed representations)

class LiveStockDetailSerializer(serializers.ModelSerializer):
    livestock_type = LiveStockTypeSerializer()
    profile = AnimalProfileSerializer()
    milk_records = MilkProductionSerializer(many=True)
    vaccinations = VaccinationRecordSerializer(many=True)
    events = EventSerializer(many=True)
    death_record = DeathRecordSerializer() # Use a SerializerMethodField if you want to conditionally serialize

    class Meta:
        model = LiveStock
        fields = '__all__'


class BreedingRecordDetailSerializer(serializers.ModelSerializer):
    sire = LiveStockSerializer()
    dam = LiveStockSerializer()
    offspring = LiveStockSerializer()

    class Meta:
        model = BreedingRecord
        fields = '__all__'