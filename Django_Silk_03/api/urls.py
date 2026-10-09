from django.urls import path
from .views import ResumeListView, UserListView

urlpatterns = [
    path("resumes/", ResumeListView.as_view(), name="ResumeListView"),
    path("users/", UserListView.as_view(), name="UserListView"),
]
