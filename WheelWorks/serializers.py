from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Vehicle, UserProfile


class OwnerSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name']


class VehicleSerializerResponse(serializers.ModelSerializer):
    owner = OwnerSerializerResponse(many=False)

    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'VIN', 'model', 'mileage', 'owner', 'color', 'year', 'owner']


class VehicleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Vehicle
        fields = ['make', 'VIN', 'model', 'mileage', 'color', 'year']

    def create(self, validated_data):
        vehicle = Vehicle.objects.create(
            make=validated_data.get('make', None),
            VIN=validated_data.get('VIN', None),
            model=validated_data.get('model', None),
            color=validated_data.get('color', None),
            year=validated_data.get('year', None),
            owner=self.context.get('owner', None),
            mileage = validated_data.get('mileage', None)
        )
        return vehicle

    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.VIN = validated_data.get('VIN', instance.VIN)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.year = validated_data.get('year', instance.year)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.save()
        return instance


