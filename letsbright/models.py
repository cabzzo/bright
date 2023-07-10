from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)  # Corrected here

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

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