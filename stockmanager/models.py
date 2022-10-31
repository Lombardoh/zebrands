from queue import Empty
from django.db import models
from zebrands.utils import product_update_email
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Product(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  sku = models.IntegerField()
  anonymous_query = models.IntegerField(default=0)

@receiver(pre_save, sender=Product)
def on_change(sender, instance: Product, **kwargs):
  try:
    previous = Product.objects.get(id=instance.id)
    changed_fields = []
    for field in Product._meta.get_fields():
      if getattr(instance, field.name) != getattr(previous, field.name):
        changed_fields.append(field.name)
    
    if len(changed_fields) > 0:
      product_update_email(instance.id, changed_fields)
  except:
    pass