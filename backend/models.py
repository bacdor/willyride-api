from django.db import models
from django.contrib.auth.models import AbstractUser

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
