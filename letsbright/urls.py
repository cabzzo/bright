from django.urls import path, include
from .views import (
    create_user_profile, home, about, create_space, add_product, place_order, 
    save_design, space_detail, login_view, 
    profile, settings_view, logout_view, dashboard, explore
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('create_space/', create_space, name='create_space'),
    path('add_product/<int:space_id>/', add_product, name='add_product'),
    path('space_detail/<int:space_id>/', space_detail, name='space_detail'),
    path('save_design/', save_design, name='save_design'),
    path('place_order/', place_order, name='place_order'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('settings/', settings_view, name='settings'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('explore/', explore, name='explore'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
]
