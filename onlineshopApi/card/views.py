from django.shortcuts import render
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework import generics, views


# Create your views here.

class CartItemView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
