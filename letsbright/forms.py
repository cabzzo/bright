from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import (
    Space, Design, Order, Device, Feedback, 
    UserProfile, Gamification, Integration, MachineLearning
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    age_group = forms.ChoiceField(choices=[('Teenager', 'Teenager'), ('Young Adult', 'Young Adult'), ('Adult', 'Adult'), ('Senior', 'Senior')])
    occupation = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age_group', 'occupation', 'phone_number']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'dimensions', 'configuration']

# Device Form
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type', 'configuration_details', 'connection_status']

# Feedback Form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'rating']

# User Profile Form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'preferences', 'subscription_details']

# Gamification Form
class GamificationForm(forms.ModelForm):
    class Meta:
        model = Gamification
        fields = ['points', 'level','badges','challenges_completed']

# Integration Form
class IntegrationForm(forms.ModelForm):
    class Meta:
        model = Integration
        fields = ['service_name','type','api_keys','configuration_details']


# Machine Learning Form
class MachineLearningForm(forms.ModelForm):
    class Meta:
        model = MachineLearning
        fields = [
            'name',
            'algorithm',
            'version',
            'last_trained_date',
            'accuracy',
            'resource_efficiency',
            'sustainability_score',
            'parameters',
            'sensor_data_reference',
            'training_data_reference',
            'is_real_time',
            'status',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'algorithm': forms.Select(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'last_trained_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'accuracy': forms.NumberInput(attrs={'class': 'form-control'}),
            'resource_efficiency': forms.NumberInput(attrs={'class': 'form-control'}),
            'sustainability_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'parameters': forms.Textarea(attrs={'class': 'form-control'}),
            'sensor_data_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'training_data_reference': forms.Textarea(attrs={'class': 'form-control'}),
            'is_real_time': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['name', 'description', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Device', 'quantity', 'shipping_address']
