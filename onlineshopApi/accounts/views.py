from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProfileSerializer, AddressSerializer
from .models import BaseUser, Profile, Address
from rest_framework import views
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class AddressCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]


