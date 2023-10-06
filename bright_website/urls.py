from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from django.urls import include
from letsbright.views import register
from letsbright import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('letsbright.urls')),
     path('cart.json/', views.cart_json, name='cart_json')
]