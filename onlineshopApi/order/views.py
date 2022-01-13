from django.shortcuts import render
from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework import generics, views


# Create your views here.

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
