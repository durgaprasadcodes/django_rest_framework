from rest_framework import serializers
from .models import Student, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "roll_number", "email", "subjects"]
