from rest_framework import generics, permissions
from .models import (
    LiveStockType, LiveStock, AnimalProfile, MilkProduction,
    HealthRecord, Feed, VaccinationRecord, BreedingRecord,
    DeathRecord, Event
)
from .serializers import (
    LiveStockTypeSerializer, LiveStockSerializer, AnimalProfileSerializer,
    MilkProductionSerializer, HealthRecordSerializer, FeedSerializer,
    VaccinationRecordSerializer, BreedingRecordSerializer, DeathRecordSerializer,
    EventSerializer, LiveStockDetailSerializer, BreedingRecordDetailSerializer
)

# LiveStockType Views
class LiveStockTypeListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating livestock types."""
    queryset = LiveStockType.objects.all()
    serializer_class = LiveStockTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LiveStockTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a livestock type."""
    queryset = LiveStockType.objects.all()
    serializer_class = LiveStockTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# LiveStock Views
class LiveStockListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating livestock."""
    queryset = LiveStock.objects.all()
    serializer_class = LiveStockSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LiveStockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting livestock (with details)."""
    queryset = LiveStock.objects.all()
    serializer_class = LiveStockDetailSerializer  # Use detailed serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# AnimalProfile Views
class AnimalProfileListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating animal profiles."""
    queryset = AnimalProfile.objects.all()
    serializer_class = AnimalProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AnimalProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting an animal profile."""
    queryset = AnimalProfile.objects.all()
    serializer_class = AnimalProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# MilkProduction Views
class MilkProductionListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating milk production records."""
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MilkProductionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a milk production record."""
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# HealthRecord Views
class HealthRecordListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating health records."""
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HealthRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a health record."""
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Feed Views
class FeedListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating feed records."""
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FeedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a feed record."""
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# VaccinationRecord Views
class VaccinationRecordListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating vaccination records."""
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VaccinationRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a vaccination record."""
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# BreedingRecord Views
class BreedingRecordListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating breeding records."""
    queryset = BreedingRecord.objects.all()
    serializer_class = BreedingRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BreedingRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a breeding record (with details)."""
    queryset = BreedingRecord.objects.all()
    serializer_class = BreedingRecordDetailSerializer  # Use detailed serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# DeathRecord Views
class DeathRecordListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating death records."""
    queryset = DeathRecord.objects.all()
    serializer_class = DeathRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DeathRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a death record."""
    queryset = DeathRecord.objects.all()
    serializer_class = DeathRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Event Views
class EventListCreateView(generics.ListCreateAPIView):
    """API endpoint for listing and creating events."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting an event."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]