from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Space, Product, Design, Order

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    occupation = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'occupation', 'phone_number']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name', 'dimensions', 'configuration']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['name', 'description', 'image']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'shipping_address']
