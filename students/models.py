from django.db import models

# Create your models here.
from core.models import User


class Student(models.Model):
    user = models.OneToOneField(User, models.CASCADE, 'student_profile', null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль студента"
        verbose_name_plural = "Профили студентов"
