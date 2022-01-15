from rest_framework.serializers import ModelSerializer
from .models import (
    Cart,
    CartItem,
)
from products.serializers import ProductSerializer


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'profile', 'completed', 'totalcart']

    def get_totalcart(self, obj):
        return obj


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'created_date']
