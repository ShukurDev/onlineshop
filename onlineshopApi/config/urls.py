from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework import permissions  # new
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('card.urls')),
    path('api/v1/', include('order.urls')),
]
