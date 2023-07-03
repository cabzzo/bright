 
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def base(request):
    return render(request, 'base.html')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm(request)
    return render(request, 'registration/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
