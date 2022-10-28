from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from stockmanager.models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'