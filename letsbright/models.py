
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .default_profiles import DEFAULT_PROFILES 


# Users and UserProfile
class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
    ('new_nihilist', 'New Nihilist'),
    ('pioneer', 'Pioneer'),
    ('time_keeper', 'Time Keeper'),
    ('reductionist', 'Reductionist'),
    ('dreamer', 'Dreamer'),
    ('rebel', 'Rebel'),
    ('maestro', 'Maestro'),
    ('builder', 'Builder'),
    ('entity', 'Entity'),
    ('crusader', 'Crusader'),
         
]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='new_nihilist')  # or another default
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/')
    preferences = models.JSONField(default=dict)
    subscription_details = models.JSONField(default=dict)
    # Fields from your existing UserProfile model
    psychographics = models.TextField(blank=True)
    needs_pain_points = models.TextField(blank=True)
    goals_dreams = models.TextField(blank=True)
    universal_themes = models.TextField(blank=True)
    outcomes = models.TextField(blank=True)
    # ... (many other fields from your existing UserProfile model)
    age_group = models.CharField(max_length=50, blank=True)
    medium = models.CharField(max_length=50, blank=True)
    style = models.CharField(max_length=50, blank=True)
    color_palette = models.CharField(max_length=50, blank=True)
    music = models.CharField(max_length=50, blank=True)
    journey_focus = models.CharField(max_length=50, blank=True)
    user_flows = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Device and Sensor
class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=255)
    configuration_details = models.JSONField(default=dict)
    connection_status = models.BooleanField(default=False)

class Sensor(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=40)
    data = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

# Space
class Space(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    space_type = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=100)
    configuration = models.TextField(default="")

# Content
class Content(models.Model):
    content_type = models.CharField(max_length=255)
    content_details = models.TextField(default="")
    associated_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

# Gamification
class Gamification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    badges = models.JSONField(default=dict)
    challenges_completed = models.IntegerField(default=0)

# Integration
class Integration(models.Model):
    service_name = models.CharField(max_length=255)
    type = models.JSONField(default=dict)
    api_keys = models.JSONField(default=dict)
    configuration_details = models.JSONField(default=dict)

# Feedback
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_details = models.TextField(default="")
    rating = models.IntegerField(default=0)
    content = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)

from django.db import models

class MachineLearning(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('testing', 'Testing'),
    ]
    
    ALGORITHM_CHOICES = [
        ('svm', 'Support Vector Machine'),
        ('rf', 'Random Forest'),
        # Add other algorithms here
    ]

    # Basic Info
    name = models.CharField(max_length=255)
    algorithm = models.CharField(max_length=50, choices=ALGORITHM_CHOICES)
    version = models.CharField(max_length=50)

    # Metrics and Performance
    last_trained_date = models.DateTimeField(default=timezone.now)
    accuracy = models.FloatField(default=0.0)
    resource_efficiency = models.FloatField(default=0.0)  # e.g., in FLOPS or similar metrics
    sustainability_score = models.FloatField(null=True, blank=True)  # Optional

    # Training and Data
    parameters = models.JSONField(default=dict)
    sensor_data_reference = models.CharField(max_length=255)
    training_data_reference = models.TextField(default="")

    # Operational flags
    is_real_time = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.algorithm}) - {self.status}"


class Order(models.Model):
    Device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    shipping_address = models.TextField(default="")

# Design
class Design(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='designs/')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Default to 'new_nihilist' if 'user_type' is not present on the User instance
        user_type = getattr(instance, 'user_type', 'new_nihilist')
        profile_data = DEFAULT_PROFILES.get(user_type, {})
        UserProfile.objects.create(user=instance, **profile_data)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
