from rest_framework import generics,viewsets
from data_management.models import LiveStock, MilkProduction
from data_management.serializers import Feed,FeedSerializer,HealthRecord,HealthRecordSerializer, HealthRecord, LivestockSerializer,MilkProductionSerializer
from django.contrib import messages
from .models import LiveStock, AnimalProfile, MilkProduction, HealthRecord, Feed
from .forms import LiveStockForm, AnimalProfileForm, MilkProductionForm, HealthRecordForm, FeedForm
from django.shortcuts import render, redirect


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



def livestock_list(request):
    livestock = LiveStock.objects.all()
    return render(request, 'livestock/livestock_list.html', {'livestock': livestock})

def livestock_create(request):
    if request.method == 'POST':
        form = LiveStockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livestock created successfully!')
            return redirect('livestock_list')
    else:
        form = LiveStockForm()
    return render(request, 'livestock/livestock_form.html', {'form': form})

def livestock_detail(request, pk):
    livestock = LiveStock.objects.get(pk=pk)
    return render(request, 'livestock/livestock_detail.html', {'livestock': livestock})

def animalprofile_list(request):
    animalprofiles = AnimalProfile.objects.all()
    return render(request, 'animalprofile/animalprofile_list.html', {'animalprofiles': animalprofiles})

def animalprofile_create(request):
    if request.method == 'POST':
        form = AnimalProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal Profile created successfully!')
            return redirect('animalprofile_list')
    else:
        form = AnimalProfileForm()
    return render(request, 'animalprofile/animalprofile_form.html', {'form': form})

def animalprofile_detail(request, pk):
    animalprofile = AnimalProfile.objects.get(pk=pk)
    return render(request, 'animalprofile/animalprofile_detail.html', {'animalprofile': animalprofile})

def milkproduction_list(request):
    milkproductions = MilkProduction.objects.all()
    return render(request, 'milkproduction/milkproduction_list.html', {'milkproductions': milkproductions})

def milkproduction_create(request):
    if request.method == 'POST':
        form = MilkProductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Milk Production record created successfully!')
            return redirect('milkproduction_list')
    else:
        form = MilkProductionForm()
    return render(request, 'milkproduction/milkproduction_form.html', {'form': form})

def milkproduction_detail(request, pk):
    milkproduction = MilkProduction.objects.get(pk=pk)
    return render(request, 'milkproduction/milkproduction_detail.html', {'milkproduction': milkproduction})

def healthrecord_list(request):
    healthrecords = HealthRecord.objects.all()
    return render(request, 'healthrecord/healthrecord_list.html', {'healthrecords': healthrecords})

def healthrecord_create(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Health Record created successfully!')
            return redirect('healthrecord_list')
    else:
        form = HealthRecordForm()
    return render(request, 'healthrecord/healthrecord_form.html', {'form': form})

def healthrecord_detail(request, pk):
    healthrecord = HealthRecord.objects.get(pk=pk)
    return render(request, 'healthrecord/healthrecord_detail.html', {'healthrecord': healthrecord})

def feed_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feed/feed_list.html', {'feeds': feeds})

def feed_create(request):
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feed created successfully!')
            return redirect('feed_list')
    else:
        form = FeedForm()
    return render(request, 'feed/feed_form.html', {'form':form})