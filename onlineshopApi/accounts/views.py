from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProfileSerializer, AddressSerializer
from .models import BaseUser, Profile, Address
from card.models import Cart
from rest_framework import views
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db import transaction

class CreateUserView(generics.CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer
    @transaction.atomic
    def perform_create(self, serializer):
        user = serializer.save()
        profile = Profile.objects.create(
            user=user,
            name='',
            photo='',
            phone='',
            description='',
            gender='',
            birth_date='',
        )

        cart = Cart.objects.create(
            profile=profile,
            completed=True,
        )
        super(CreateUserView, self).perform_create()


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []


class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
