from django.shortcuts import render
from rest_framework import generics, mixins, views
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response


# Create your views here.

class DashboardView(generics.GenericAPIView,
                    mixins.ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
