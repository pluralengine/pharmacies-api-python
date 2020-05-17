from rest_framework import serializers
from .models import Pharmacy
from products.models import Product


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'name', 'address', 'phone_num', 'areas',
                  'geometry_lat', 'geometry_lng', 'products']

    def create(self, validated_data):
        return Pharmacy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phoneNum = validated_data.get('phoneNum', instance.phoneNum)
        instance.areas = validated_data.get('areas', instance.areas)
        instance.geometry_lat = validated_data.get(
            'geometry_lat', instance.geometry_lat)
        instance.geometry_lng = validated_data.get(
            'geometry_lng', instance.geometry_lng)
        instance.save()
        return instance
