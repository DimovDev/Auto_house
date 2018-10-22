from rest_framework import serializers

from .models import Category ,Vehicles


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = (
            'category', 'Brand', 'Model', 'Year_of_production', 'Engine', 'Transmission', 'image', 'description',
            'price', 'stock', 'available', 'created', 'updated')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name', 'slug',)
