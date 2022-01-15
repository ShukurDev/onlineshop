from .models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    cart_total = serializers.SerializerMethodField()
    cart_items = serializers.SerializerMethodField()

    class Meta:
            model = Order
            fields = ['user', 'ordered', 'date_created', 'barcode', 'region', 'city', 'district', 'state',
                      'target', 'cart_total', 'cart_items']
    # def get_address(self, value):
    #     if value:
    #         return value
    #     else:

    def get_cart_items(self, obj):
        return obj.cart_items

    def get_cart_total(self, obj):
        return obj.cart_total

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'date_added']


class OrderItemStatis(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('id', 'total_sum', 'price', 'quantity', 'total_sum')

    def total_sum(self, obj):

        return obj.total_sum
