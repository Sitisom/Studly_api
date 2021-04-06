
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from core.roles import Role


class User(AbstractUser):
    role = models.CharField(max_length=30, choices=Role.as_choices(), null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
