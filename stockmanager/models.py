from statistics import mode
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  sku = models.IntegerField()
