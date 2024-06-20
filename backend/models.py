from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    car_color = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.is_driver:
            self.car_model = None
            self.car_color = None
        super().save(*args, **kwargs)

class RideRequest(models.Model):
    passenger = models.ForeignKey('User', on_delete=models.CASCADE, related_name='ride_requests')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField()
    seats_requested = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=500, null=True, blank=True)

class RideOffer(models.Model):
    driver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='ride_offers')
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField()
    available_seats = models.IntegerField(validators=[MinValueValidator(0)])
    ride_fare = models.DecimalField(max_digits=6, decimal_places=2, default=0, validators=[MinValueValidator(0)])
