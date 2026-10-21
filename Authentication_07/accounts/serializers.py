from rest_framework import serializers
from .models import User, Profile
import re


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["name", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        password = attrs.get("password", "")

        if len(password) < 8:
            raise serializers.ValidationError(
                "Password must contain at least 8 characters."
            )

        if not re.search(r"[A-Z]", password):
            raise serializers.ValidationError(
                "Password must contain an uppercase letter."
            )

        if not re.search(r"[a-z]", password):
            raise serializers.ValidationError(
                "Password must contain a lowercase letter."
            )

        if not re.search(r"\d", password):
            raise serializers.ValidationError(
                "Password must contain a numerical digit."
            )

        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "bio"]
