# Generated by Django 3.0.6 on 2020-05-17 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0002_pharmacy_products'),
        ('users', '0002_auto_20200517_0950'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
