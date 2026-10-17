from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class PublicAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Anyone can access this API"})


class PrivateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {"message": "You are authenticated", "user": request.user.username}
        )


class AdminAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response(
            {
                "username": request.user.username,
                "is_authenticated": request.user.is_authenticated,
                "is_staff": request.user.is_staff,
                "auth": str(request.auth),
            }
        )
