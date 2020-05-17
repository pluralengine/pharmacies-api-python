# Generated by Django 3.0.6 on 2020-05-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('pharmacies', '0002_pharmacy_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
