from rest_framework import serializers
from tutorials.models import Product 
from tutorials.models import Shopcart

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'amount')
class ShopcartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopcart
        fields = ('id',
                  'productId',
                  'quantity' )        