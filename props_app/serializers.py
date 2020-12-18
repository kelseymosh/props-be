from rest_framework import serializers
from .models import User, Plant, Favorite
from django.contrib.auth.hashers import make_password


class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name')


class PlantObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name', 'img', 'description', 'users', 'favorites')


class FavoriteObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'plant')


class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'full_name', 'favorites')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password'],
            full_name = validated_data['full_name']
        )
        user.save()
        return user


class PlantSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    # favorites = FavoriteObjectSerializer(many=True)
    
    class Meta:
        model = Plant
        fields = ('id', 'name', 'img', 'description', 'users')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'plant')

