from django.db import models
from django.apps import apps
from pharmacies.models import Pharmacy

# Register your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    automatically_created = models.BooleanField(default=False)
    pharmacy = models.OneToOneField(
        Pharmacy, on_delete=models.CASCADE, primary_key=True)
