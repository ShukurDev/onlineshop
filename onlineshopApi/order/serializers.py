from .models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['user', 'ordered', 'address', 'date_created', 'barcode', 'region', 'city', 'district', 'state',
                  'target']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'date_create']
