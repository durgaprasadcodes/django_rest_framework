from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer


class StudentGenericView(generics.ListAPIView):
    queryset = Student.objects.prefetch_related("subjects")
    serializer_class = StudentSerializer


class SingleStudentGenericView(generics.RetrieveAPIView):
    queryset = Student.objects.prefetch_related("subjects")
    serializer_class = StudentSerializer
