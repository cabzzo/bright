from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Sensor(models.Model):
    SENSOR_TYPES = (
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('motion', 'Motion'),
        ('light', 'Light'),
        ('air', 'Air Quality'),
        ('sound', 'Sound Level'),
    )
    
    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=40, choices=SENSOR_TYPES)
    data = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Space(models.Model):
    name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    configuration = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Design(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='designs/')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    shipping_address = models.TextField()

   
AUDIENCE_TYPE_CHOICES = [
        ('new_nihilist', 'The New Nihilists'),
        ('pioneer', 'The Pioneers'),
        ('time_keeper', 'The Time Keepers'),
        ('reductionist', 'The Reductionists'),
        ('dreamer', 'The Dreamers' ),
        ('rebel', 'The Rebels'),
        ('Maestro', 'Design Maestros'),
        ('builder', 'The Builders'),
            ]

    
    
    # Fields specific to certain audience types
seeking_meaning = models.BooleanField(default=False, blank=True)
    # ... add more
    
    # Fields for industry professionals
is_design_maestro = models.BooleanField(default=False, blank=True)
is_builder = models.BooleanField(default=False, blank=True)
    # ... add more
    
    # Fields for institutional profiles
is_government_entity = models.BooleanField(default=False, blank=True)
is_corporate_crusader = models.BooleanField(default=False, blank=True)
    # ... add more


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    psychographics = models.TextField(blank=True)
    needs_pain_points = models.TextField(blank=True)
    goals_dreams = models.TextField(blank=True)
    universal_themes = models.TextField(blank=True)
    outcomes = models.TextField(blank=True)
    medium = models.CharField(max_length=50, blank=True)
    style = models.CharField(max_length=50, blank=True)
    color_palette = models.CharField(max_length=50, blank=True)
    music = models.CharField(max_length=50, blank=True)
    journey_focus = models.CharField(max_length=50, blank=True)
    user_flows = models.TextField(blank=True)
    
    # Cross-Referenced Fields for Ad Targeting
    location = models.CharField(max_length=50, blank=True)  # Maps to User Flows
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    interests = models.TextField(blank=True)  # Aligns with Medium, Style, Music
    online_behavior = models.TextField(blank=True)  # Correlates with Journey Focus, User Flows
    device_platform = models.CharField(max_length=50, blank=True)  # Subset of Online Behavior
    income_level = models.CharField(max_length=50, blank=True)  # Inferred from Job Role & Industry
    job_role = models.CharField(max_length=50, blank=True)
    industry = models.CharField(max_length=50, blank=True)  # Ties to Psychographics and Needs
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    audience_type = models.CharField(max_length=50, choices=AUDIENCE_TYPE_CHOICES, blank=True)
    user_type = models.CharField(max_length=50, choices=AUDIENCE_TYPE_CHOICES, blank=True)
    music_preference = models.CharField(max_length=20, blank=True)

# Signals to create and update the UserProfile when a User is created or updated
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


    def __str__(self):
        return f"{self.user.username}'s Profile"
    