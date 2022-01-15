from .models import BaseUser, Profile, Address
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = BaseUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = BaseUser
        fields = ('password', 'username', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'photo', 'phone', 'description', 'gender', 'birth_date')
        extra_kwargs = {'phone': {'read_only': True, 'max_length': 13}}


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('profile', 'region', 'city', 'district', 'state', 'address', 'date_created')

