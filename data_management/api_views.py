from rest_framework import generics, viewsets
from .models import LiveStock, MilkProduction, HealthRecord, Feed
from .serializers import FeedSerializer, HealthRecordSerializer, LivestockSerializer, MilkProductionSerializer

class LivestockListCreateView(generics.ListCreateAPIView):
    queryset = LiveStock.objects.all()
    serializer_class = LivestockSerializer

class LivestockDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LiveStock.objects.all()
    serializer_class = LivestockSerializer

class MilkProductionListCreateView(generics.ListCreateAPIView):
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer

class MilkProductionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer