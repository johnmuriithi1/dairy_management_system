from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCReationForm, FarmerProfileForm, FarmAgentProfileForm, VeterinaryPartnerProfileForm
from .models import Farmer, FarmAgent, VeterinaryPartner, User

def home(request):
    return render(request, 'users_management/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'users_management/login.html')

def user_logout(request):
    logout(request)
    return render(request, 'users_management/logout.html')

def create_user(request):
    if request.method == 'POST':
        form = UserCReationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_type = form.cleaned_data['user_type']  # Get user_type from form data
            user.save()

            if user.user_type == 1:  # Farmer
                # Generate a unique farmer_code (example)
                import uuid
                farmer_code = str(uuid.uuid4())[:8]
                farmer = Farmer(user=user, farmer_code=farmer_code)
                farmer.save()
                messages.success(request, 'Farmer user created successfully!')
                return redirect('complete_farmer_profile')

            elif user.user_type == 2:  # FarmAgent
                user.save()
                farm_agent = FarmAgent(user=user)
                farm_agent.save()
                messages.success(request, 'Farm Agent user created successfully!')
                return redirect('complete_farm_agent_profile')

            elif user.user_type == 3:  # VeterinaryPartner
                user.save()
                veterinary_partner = VeterinaryPartner(user=user)
                veterinary_partner.save()
                messages.success(request, 'Veterinary Partner user created successfully!')
                return redirect('complete_veterinary_partner_profile')

            else:
                messages.error(request, "Invalid user type.")
                return redirect('create_user')

        else:
            context = {'form': form}
            return render(request, 'users_management/create_user.html', context)
    else:
        form = UserCReationForm()
    return render(request, 'users_management/create_user.html', {'form': form})

def user_dashboard(request):
    user = request.user
    farmer = None
    farm_agent = None
    veterinary_partner = None

    if user.user_type == 1:  # Farmer
        farmer = get_object_or_404(Farmer, user=user)
    elif user.user_type == 2:  # Farm Agent
        farm_agent = get_object_or_404(FarmAgent, user=user)
    elif user.user_type == 3:  # Veterinary Partner
        veterinary_partner = get_object_or_404(VeterinaryPartner, user=user)

    context = {
        'user': user,
        'farmer': farmer,
        'farm_agent': farm_agent,
        'veterinary_partner': veterinary_partner,
    }
    return render(request, 'users_management/dashboard.html', context)


def edit_profile(request):
    user = request.user
    user_type = user.user_type

    if user_type == 1:
        try:
            farmer = Farmer.objects.get(user=user)
        except Farmer.DoesNotExist:
            messages.error(request, "Farmer profile not found.")
            return redirect('complete_farmer_profile')
        form = FarmerProfileForm(request.POST or None, instance=farmer) 
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated successfully!')
            return redirect('dashboard')
        return render(request, 'users_management/profile_edit.html', {'form': form})

    elif user_type == 2:
        try:
            farm_agent = FarmAgent.objects.get(user=user)
        except FarmAgent.DoesNotExist:
            messages.error(request, "Farm Agent profile not found.")
            return redirect('complete_farm_agent_profile')
        form = FarmAgentProfileForm(request.POST or None, instance=farm_agent)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated successfully!')
            return redirect('dashboard')
        return render(request, 'users_management/profile_edit.html', {'form': form})

    elif user_type == 3:
        try:
            veterinary_partner = VeterinaryPartner.objects.get(user=user)
        except VeterinaryPartner.DoesNotExist:
            messages.error(request, "Veterinary Partner profile not found.")
            return redirect('complete_veterinary_partner_profile')
        form = VeterinaryPartnerProfileForm(request.POST or None, instance=veterinary_partner)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated successfully!')
            return redirect('dashboard')
        return render(request, 'users_management/profile_edit.html', {'form': form})

    else:
        messages.error(request, "Unknown user type.")
        return redirect('dashboard') 

def complete_veterinary_partner_profile(request):
    if request.method == 'POST':
        form = VeterinaryPartnerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new VeterinaryPartner instance 
            veterinary_partner = VeterinaryPartner(user=request.user) 
            form.save(commit=False) 
            veterinary_partner.save() 
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = VeterinaryPartnerProfileForm()
    return render(request, 'users_management/complete_veterinary_partner_profile.html', {'form': form}) 

def complete_farm_agent_profile(request):
    if request.method == 'POST':
        form = FarmAgentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new FarmAgent instance 
            farm_agent = FarmAgent(user=request.user) 
            form.save(commit=False) 
            farm_agent.save() 
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = FarmAgentProfileForm()
    return render(request, 'users_management/complete_farm_agent_profile.html', {'form': form}) 

def complete_farmer_profile(request):
    if request.method == 'POST':
        form = FarmerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new Farmer instance associated with the current user
            farmer = Farmer(user=request.user) 
            form.save(commit=False) 
            farmer.save() 
            messages.success(request, 'Farmer profile created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = FarmerProfileForm()
    return render(request, 'users_management/complete_farmer_profile.html', {'form': form})