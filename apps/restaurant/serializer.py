from rest_framework import serializers
from .models import (
    Restaurant, Category, Product, Details
)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    product = serializers.CharField()
    size = serializers.CharField()
    cost = serializers.CharField()

    class Meta:
        model = Details
        fields = ('product', 'size', 'cost')
