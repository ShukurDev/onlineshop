from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'parent', 'description', 'slug', 'date_created', 'activate']

    # def validate_category(self, value):
    #     if self.initial_data.get('parent') is None:
    #         return value
    #     else:
    #         result = self.initial_data.get('parent')
    #         result.delete()
    #         return result


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'photo', 'description', 'date_created']
