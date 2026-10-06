from rest_framework import serializers
from .models import Category, Tour


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'title', 'description', 'category', 'price', 'duration_day', 'location', 'created_at']
