from django.db import models

# Create your models here.
from core.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль студента"
        verbose_name_plural = "Профили студентов"
