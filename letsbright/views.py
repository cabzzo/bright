from telnetlib import LOGOUT
from .forms import (
    RegistrationForm, LoginForm, SpaceForm, 
    DesignForm, OrderForm, DeviceForm,
    FeedbackForm, UserProfileForm, GamificationForm,
    IntegrationForm, MachineLearningForm
)
from .quiz_forms import OnboardingQuizForm

from .models import Space, Device, Feedback, UserProfile, Gamification, Integration, MachineLearning
from django.http import JsonResponse, HttpResponse
from django.shortcuts import (
    redirect, render, get_object_or_404, redirect,
)

from django.contrib.auth import (
    authenticate, login, logout,
)

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import logging

logger = logging.getLogger(__name__)

# Home
def home(request):
    return render(request, 'home.html')

# Dashboard for logged-in users
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Profile for logged-in users
@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Redirect to a page where the user can create a profile, or show a message
        return redirect('create_user_profile')
    
    connected_devices = Device.objects.filter(user=request.user)
    spaces = Space.objects.filter(user=request.user)
    educational_content = Content.objects.filter(user=request.user)  # make sure Content model is imported
    badges = Gamification.objects.filter(user=request.user).values_list('badge', flat=True)
    
    context = {
        'user_profile': user_profile,
        'connected_devices': connected_devices,
        'spaces': spaces,
        'educational_content': educational_content,
        'badges': badges,
    }
    return render(request, 'profile.html', context)

# Settings for logged-in users
@login_required
def settings(request):
    return render(request, 'settings.html')

# Explore for all users
def explore(request):
    return render(request, 'explore.html')

def login_view(request):
    logger.debug('Entering login_view')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            logger.debug('Form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                logger.debug(f'Authenticated user {username}')
                login(request, user)
                return redirect('dashboard')
            else:
                logger.warning(f'Failed to authenticate user {username}')
                
        else:
            logger.warning('Form is not valid')
            logger.warning(form.errors)
    else:
        form = LoginForm(request)
        
    return render(request, 'registration/login.html', {'form': form})

# Create Space
def create_space(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            space = form.save()
            return redirect('space_detail', space_id=space.pk)
    else:
        form = SpaceForm()
    return render(request, 'create_space.html', {'form': form})

# Create Device
def add_device(request, space_id):
    if request.method == 'POST':
        form = DeviceForm(request.POST)  # Changed from ProductForm to DeviceForm
        if form.is_valid():
            device = form.save(commit=False)
            device.space_id = space_id
            device.save()
            return redirect('space_detail', space_id=space_id)
    else:
        form = DeviceForm()  # Changed from ProductForm to DeviceForm
    return render(request, 'add_device.html', {'form': form})


# Create Feedback
@login_required
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('dashboard')
    else:
        form = FeedbackForm()
    return render(request, 'create_feedback.html', {'form': form})

# Update User Profile
@login_required
def update_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    return render(request, 'update_user_profile.html', {'form': form})

# Create Gamification
@login_required
def create_gamification(request):
    if request.method == 'POST':
        form = GamificationForm(request.POST)
        if form.is_valid():
            gamification = form.save(commit=False)
            gamification.user = request.user
            gamification.save()
            return redirect('dashboard')
    else:
        form = GamificationForm()
    return render(request, 'create_gamification.html', {'form': form})

# Create Integration
@login_required
def create_integration(request):
    if request.method == 'POST':
        form = IntegrationForm(request.POST)
        if form.is_valid():
            integration = form.save()
            return redirect('dashboard')
    else:
        form = IntegrationForm()
    return render(request, 'create_integration.html', {'form': form})

# Create Machine Learning
@login_required
def create_machine_learning(request):
    if request.method == 'POST':
        form = MachineLearningForm(request.POST)
        if form.is_valid():
            machine_learning = form.save()
            return redirect('dashboard')
    else:
        form = MachineLearningForm()
    return render(request, 'create_machine_learning.html', {'form': form})


# Space Detail
def space_detail(request, space_id):
    space = get_object_or_404(Space, pk=space_id)
    return render(request, 'space_detail.html', {'space': space})

# Save Design
def save_design(request):
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save()
            return redirect('design_detail', design_id=design.pk)
    else:
        form = DesignForm()
    return render(request, 'save_design.html', {'form': form})

# Place Order
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.pk)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})

# Cart JSON
def cart_json(request):
    cart_data = {
        "item": "Example Item",
        "quantity": 2,
    }
    return JsonResponse(cart_data)

# About
def about(request):
    return render(request, 'about.html')


# Settings View
@login_required
def settings_view(request):
    return render(request, 'settings.html')

def create_user_profile(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            print("Form is valid. Redirecting to onboarding.")  # Debug print
            return redirect('onboarding')  # Redirect to onboarding
        else:
            print("Form is invalid.")  # Debug print
            print(user_form.errors)  # Print the errors

    else:
        user_form = RegistrationForm()
    
    return render(request, 'create_user_profile.html', {'user_form': user_form})

def logout_view(request):
    logout(request)
    return redirect('home')


def onboarding(request):
    if request.method == 'POST':
        form = OnboardingQuizForm(request.POST)
        if form.is_valid():
            # Handle form submission and redirect
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = OnboardingQuizForm()

    return render(request, 'onboarding.html', {'form': form})


@login_required
def dashboard_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    connected_devices = Device.objects.filter(user=request.user)
    spaces = Space.objects.filter(user=request.user)
    # Add gamification logic here
    context = {
        'user_profile': user_profile,
        'connected_devices': connected_devices,
        'spaces': spaces,
    }
    return render(request, 'dashboard.html', context)

@login_required
def submit_quiz(request):
    print("submit_quiz called")  # Debug line
    try:
        if request.method == 'POST':
            print(request.POST)  # Debug line

            answers = {
                'focus_aspiration': request.POST.get('focus_aspiration'),
                'values': request.POST.get('values'),
                'learning_medium': request.POST.get('learning_medium'),
                'style': request.POST.get('style'),
                'outcomes': request.POST.get('outcomes')
            }

            profile = UserProfile.objects.get(user=request.user)
            profile.quiz_answers = answers
            profile.save()

            return JsonResponse({'status': 'success'})
    except Exception as e:
        print(e)  # Debug line
        return JsonResponse({'status': 'failed'}, status=400)