from django.urls import path
from letsbright import views
from .views import register


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
