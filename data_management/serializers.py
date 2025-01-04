from rest_framework import serializers
from .models import LiveStock, MilkProduction, Feed, HealthRecord

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStock
        fields = '__all__'

    def validate(self, data):
        """
        Check that if animal_type is 'other', other_animal_type is provided.
        """
        if data.get('animal_type') == 'other' and not data.get('other_animal_type'):
            raise serializers.ValidationError({"other_animal_type": "Please specify the animal type when 'Other' is selected."})
        elif data.get('animal_type') != 'other':
            data['other_animal_type'] = None  # Clear other_animal_type if not needed
        return data

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