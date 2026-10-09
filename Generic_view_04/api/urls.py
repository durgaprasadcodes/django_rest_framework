from django.urls import path
from .views import StudentGenericView, SingleStudentGenericView

urlpatterns = [
    path("", StudentGenericView.as_view()),
    path("<str:pk>", SingleStudentGenericView.as_view()),
]
