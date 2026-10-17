from django.urls import path
from .views import PublicAPI, PrivateAPI, AdminAPI

urlpatterns = [
    path("public/", PublicAPI.as_view()),
    path("private/", PrivateAPI.as_view()),
    path("admin/", AdminAPI.as_view()),
]
