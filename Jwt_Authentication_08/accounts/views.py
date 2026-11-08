from .models import User
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import status


class Registration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "user registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
