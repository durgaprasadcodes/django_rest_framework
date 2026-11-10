from django.urls import path
from .views import Registration, ProfileView

urlpatterns = [
    path("register/", Registration.as_view()),
    path("profile/", ProfileView.as_view()),
]
