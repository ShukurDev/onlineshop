from rest_framework.serializers import ModelSerializer
from .models import (
    Cart,
    CartItem,
)


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'completed']


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'created_date']
