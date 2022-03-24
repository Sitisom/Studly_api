
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from core.roles import Role


class DefaultAbstractFields(models.Model):
    created_at = models.DateTimeField("Время создания", auto_created=True)
    updated_at = models.DateTimeField("Время обновления", auto_now_add=True)


class User(AbstractUser):
    role = models.CharField(max_length=30, choices=Role.as_choices(), null=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        try:
            Rating.objects.get(user=self)
        except Rating.DoesNotExist:
            Rating.objects.create(user=self)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rating')
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
