from .models import BaseUser, Profile, Address
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['username', 'email']


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

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'photo', 'phone', 'description', 'gender', 'birth_date')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('profile', 'region', 'city', 'district', 'state', 'address', 'date_created')
