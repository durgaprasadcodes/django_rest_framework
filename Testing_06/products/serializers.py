from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Products


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "is_active", "is_staff", "is_superuser"]


class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ["id", "name", "price", "owner"]
