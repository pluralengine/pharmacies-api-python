from django.db import models

# Register your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
