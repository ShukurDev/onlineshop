from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, OrderStatisSerializer
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# 1 ta problem
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderStatisView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatisSerializer


class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = []


class OrderItemStatis(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
