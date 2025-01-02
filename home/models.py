from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.email 
    
class CarbonFootprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    electricity = models.FloatField(default=0.0)  # kWh
    natural_gas = models.FloatField(default=0.0)  # in cubic meters
    heating_oil = models.FloatField(default=0.0)  # liters
    coal = models.FloatField(default=0.0)  # kg
    lpg = models.FloatField(default=0.0)  # liters
    propane = models.FloatField(default=0.0)  # liters
    wood = models.FloatField(default=0.0)  # kg
    total_footprint = models.FloatField(default=0.0)  # Total emissions in tonnes of CO₂
    date = models.DateField(auto_now_add=True)  # Automatically set the entry date

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.total_footprint:.2f} tonnes CO₂"