import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Resume(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "resume_name"], name="unique_resume_name_per_user"
            )
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resume_link = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    resume_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    is_primary_resume = models.BooleanField(default=False)
