from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
]
