from django.shortcuts import render
from .models import Resume, User
from .serializers import ResumeSerializer, UserWithResumesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ResumeListView(APIView):
    def get(self, request):
        resumes = Resume.objects.select_related("user")
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save()
            return Response(ResumeSerializer(resume).data)
        return Response(serializer.errors, status=400)


class UserListView(APIView):
    def get(self, request):
        users = User.objects.prefetch_related("resumes")
        serializer = UserWithResumesSerializer(users, many=True)
        return Response(serializer.data)
