from rest_framework import serializers
from .models import Fruit, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['id', 'name', 'region_id']