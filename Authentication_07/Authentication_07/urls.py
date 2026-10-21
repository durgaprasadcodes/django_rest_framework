from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair_view"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh_view"),
]
