from django.urls import path
from .views import register, home, about  # Import the necessary view functions

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
