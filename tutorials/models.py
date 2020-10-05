from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    price = models.FloatField()
    amount = models.IntegerField()

class Shopcart(models.Model):
    productId = models.IntegerField()
    quantity = models.IntegerField() 
     