
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from core.roles import Role


class DefaultAbstractFields(models.Model):
    created_at = models.DateTimeField("Время создания", auto_created=True)
    updated_at = models.DateTimeField("Время обновления", auto_now_add=True)


class User(AbstractUser):
    role = models.CharField("Роль", max_length=30, choices=Role.as_choices(), default=Role.STUDENT.value)
    avatar = models.ImageField("Аватар", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Rating(models.Model):
    user = models.ForeignKey(User, models.CASCADE, "rating", null=True)
    rating = models.IntegerField("Рейтинг", default=0)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
