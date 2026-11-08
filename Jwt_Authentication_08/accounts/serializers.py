from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["user_name", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        password = attrs.get("password", "")

        if password == "":
            raise serializers.ValidationError("password not be empty")
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        pass
