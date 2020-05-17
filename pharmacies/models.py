from django.db import models
from django.apps import apps
from products.models import Product

# Register your models here.


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    center_code = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    areas = models.CharField(max_length=255)
    provinces = models.CharField(max_length=255)
    regions_ccaa = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    geometry_lat = models.CharField(max_length=255)
    geometry_lng = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, blank=True)
