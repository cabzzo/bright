from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Existing imports
from .forms import RegistrationForm, LoginForm, SpaceForm, ProductForm, DesignForm, OrderForm
from .models import Space
from django.http import JsonResponse

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
    return render(request, 'profile.html')

# Settings for logged-in users
@login_required
def settings(request):
    return render(request, 'settings.html')

# Explore for all users
def explore(request):
    return render(request, 'explore.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm(request)
    return render(request, 'registration/login.html', {'form': form})

def create_space(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            space = form.save()
            # Perform any additional operations related to space creation
            return redirect('space_detail', space_id=space.pk)
    else:
        form = SpaceForm()
    return render(request, 'create_space.html', {'form': form})

def add_product(request, space_id):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.space_id = space_id
            product.save()
            # Perform any additional operations related to product addition
            return redirect('space_detail', space_id=space_id)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def space_detail(request, space_id):
    space = get_object_or_404(Space, pk=space_id)
    return render(request, 'space_detail.html', {'space': space})

def save_design(request):
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            design = form.save()
            # Perform any additional operations related to design saving
            return redirect('design_detail', design_id=design.pk)
    else:
        form = DesignForm()
    return render(request, 'save_design.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # Perform any additional operations related to order placement
            return redirect('order_detail', order_id=order.pk)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})
def cart_json(request):
    cart_data = {
        "item": "Example Item",
        "quantity": 2,
        # ... other cart data
    }
    return JsonResponse(cart_data)
def about(request):
    return render(request, 'about.html')
def register(request):
    # Your registration logic here
    return render(request, 'register.html')
@login_required
def settings_view(request):
    # Your settings logic here
    return render(request, 'settings.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
def create_profile(request):
    # Your logic for creating a profile
    return render(request, 'create_profile.html')
