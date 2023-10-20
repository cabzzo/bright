from django.urls import path, include
from .views import (
    create_user_profile, home, about, create_space, add_device, place_order, 
    save_design, space_detail, login_view, 
    profile, settings_view, logout_view, dashboard, explore, onboarding, create_feedback, update_user_profile, create_gamification, create_integration, create_machine_learning 
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('create_space/', create_space, name='create_space'),
    path('add_device/<int:space_id>/', add_device, name='add_device'),
    path('space_detail/<int:space_id>/', space_detail, name='space_detail'),
    path('save_design/', save_design, name='save_design'),
    path('place_order/', place_order, name='place_order'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('settings/', settings_view, name='settings'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('explore/', explore, name='explore'),
    path('create_user_profile/', create_user_profile, name='create_user_profile'),
    path('onboarding/', onboarding, name='onboarding'),
    path('create_feedback/', create_feedback, name='create_feedback'),
    path('update_profile/', update_user_profile, name='update_user_profile'),
    path('gamification/', create_gamification, name='create_gamification'),
    path('integration/', create_integration, name='create_integration'),
    path('machine_learning/', create_machine_learning, name='create_machine_learning'),
    ]

