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


class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer