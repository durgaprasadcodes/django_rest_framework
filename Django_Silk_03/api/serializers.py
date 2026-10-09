from rest_framework import serializers
from .models import User, Resume


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = Resume
        fields = [
            "id",
            "resume_link",
            "created_at",
            "resume_name",
            "user",
            "user_id",
            "is_primary_resume",
        ]


class OnlyResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = [
            "id",
            "resume_link",
            "created_at",
            "resume_name",
            "is_primary_resume",
        ]


class OnlyUserSerializers(serializers.ModelSerializer):
    resumes = OnlyResumeSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "resumes"]
