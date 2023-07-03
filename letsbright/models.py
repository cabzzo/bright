from django.db import models

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
