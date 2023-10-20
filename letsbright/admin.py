from django.contrib import admin
from .models import (
    UserProfile, Sensor, Device, Space, Device, 
    Design, Order, Integration, MachineLearning, 
    Gamification, Feedback, Content
)

# Registering UserProfile and Sensor as before
admin.site.register(UserProfile)
admin.site.register(Sensor)

# Registering new models
admin.site.register(Device)
admin.site.register(Space)
admin.site.register(Design)
admin.site.register(Order)
admin.site.register(Integration)
admin.site.register(MachineLearning)
admin.site.register(Gamification)
admin.site.register(Feedback)
admin.site.register(Content)