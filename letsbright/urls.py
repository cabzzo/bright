from django.urls import path
from .views import home, about, create_space, add_product, place_order, save_design, space_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('create_space/', create_space, name='create_space'),
    path('add_product/<int:space_id>/', add_product, name='add_product'),
    path('space_detail/<int:space_id>/', space_detail, name='space_detail'),
    path('save_design/', save_design, name='save_design'),
    path('place_order/', place_order, name='place_order'),
]
