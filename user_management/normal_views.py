from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCReationForm, FarmerProfileForm, FarmAgentProfileForm, VeterinaryPartnerProfileForm
from .models import Farmer, FarmAgent, VeterinaryPartner
import uuid 


def home(request):
    return render(request, 'users_management/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_management:dashboard')
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
            user = form.save()

            if user.user_type == 1:  # Farmer
                try:
                    farmer_code = str(uuid.uuid4())[:8]
                    farmer = Farmer(user=user, farmer_code=farmer_code)
                    farmer.save()
                    messages.success(request, 'Farmer user created successfully!')
                    return redirect('user_management:complete_farmer_profile')

                except IntegrityError:
                    messages.error(request, "A farmer with that code already exists. Please try again.")
                    user.delete() # important to delete the user if the farmer creation fails
                    return redirect('user_management:create_user') # Redirect back to the form

            elif user.user_type == 2:  # FarmAgent
                try:
                    farm_agent = FarmAgent(user=user, agent_code=str(uuid.uuid4())[:8], identification_number=str(uuid.uuid4())[:8])
                    farm_agent.save()
                    messages.success(request, 'Farm Agent user created successfully!')
                    return redirect('user_management:complete_farm_agent_profile')
                except IntegrityError:
                    messages.error(request, "A Farm Agent with that code or identification number already exists. Please try again.")
                    user.delete()
                    return redirect('user_management:create_user')

            elif user.user_type == 3:  # VeterinaryPartner
                try:
                    veterinary_partner = VeterinaryPartner(user=user)
                    veterinary_partner.save()
                    messages.success(request, 'Veterinary Partner user created successfully!')
                    return redirect('user_management:complete_veterinary_partner_profile')
                except IntegrityError: #This is unlikely for this model, but good practice to include
                    messages.error(request, "An error occurred creating the Veterinary Partner. Please try again.")
                    user.delete()
                    return redirect('user_management:create_user')

            else:
                messages.error(request, "Invalid user type.")
                user.delete()
                return redirect('user_management:create_user')
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

    # Dictionary mapping user types to model and form
    profile_data = {
        1: {'model': Farmer, 'form': FarmerProfileForm, 'redirect_url': 'complete_farmer_profile'},
        2: {'model': FarmAgent, 'form': FarmAgentProfileForm, 'redirect_url': 'complete_farm_agent_profile'},
        3: {'model': VeterinaryPartner, 'form': VeterinaryPartnerProfileForm, 'redirect_url': 'complete_veterinary_partner_profile'},
    }

    if user_type not in profile_data:
        messages.error(request, "Unknown user type.")
        return redirect('user_management:dashboard')

    data = profile_data[user_type]
    Model = data['model']
    Form = data['form']
    redirect_url = data['redirect_url']

    try:
        instance = Model.objects.get(user=user)
    except Model.DoesNotExist:
        messages.error(request, f"{Model.__name__} profile not found.")
        return redirect(redirect_url)

    form = Form(request.POST or None, request.FILES or None, instance=instance) # Added request.FILES
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Profile Updated successfully!')
        return redirect('user_management:dashboard')

    return render(request, 'users_management/profile_edit.html', {'form': form})

def complete_veterinary_partner_profile(request):
    if request.method == 'POST':
        form = VeterinaryPartnerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new VeterinaryPartner instance 
            veterinary_partner = VeterinaryPartner(user=request.user) 
            form.save(commit=False) 
            veterinary_partner.save() 
            messages.success(request, 'Profile created successfully!')
            return redirect('user_management:dashboard')  # Redirect to the dashboard
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
            return redirect('user_management:dashboard')  # Redirect to the dashboard
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
            return redirect('user_management:dashboard')  # Redirect to the dashboard
    else:
        form = FarmerProfileForm()
    return render(request, 'users_management/complete_farmer_profile.html', {'form': form})




@login_required
def profile(request):
    user = request.user
    user_type = user.user_type

    if user_type == 1:  # Farmer
        try:
            profile = Farmer.objects.get(user=user)
        except Farmer.DoesNotExist:
            return redirect('user_management:complete_farmer_profile')  # Redirect to complete profile if not found
        context = {'profile': profile, 'user_type': 'Farmer'}

    elif user_type == 2:  # Farm Agent
        try:
            profile = FarmAgent.objects.get(user=user)
        except FarmAgent.DoesNotExist:
            return redirect('user_management:complete_farm_agent_profile')
        context = {'profile': profile, 'user_type': 'Farm Agent'}

    elif user_type == 3:  # Veterinary Partner
        try:
            profile = VeterinaryPartner.objects.get(user=user)
        except VeterinaryPartner.DoesNotExist:
            return redirect('user_management:complete_veterinary_partner_profile')
        context = {'profile': profile, 'user_type': 'Veterinary Partner'}

    else:
        # Handle cases where user_type is invalid (optional)
        return redirect('user_management:dashboard')  # Or display an error message

    return render(request, 'users_management/profile.html', context)