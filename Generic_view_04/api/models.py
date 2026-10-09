from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser, BaseUserManager


class StudentManager(BaseUserManager):
    """Custom manager to handle user creation with email as the unique identifier."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Student(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid4)

    username = None

    email = models.EmailField(unique=True)

    roll_number = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "roll_number"]

    objects = StudentManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"


class Subject(models.Model):

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="subjects"
    )

    name = models.CharField(max_length=100)

    code = models.CharField(max_length=10, unique=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
