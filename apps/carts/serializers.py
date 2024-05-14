from rest_framework import serializers

from apps.carts.models import Cart,CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','user','created')
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id','cart','product','quantity')