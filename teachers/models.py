from django.db import models

# Create your models here.
from core.models import User, DefaultAbstractFields


class TeacherProfile(DefaultAbstractFields):
    user = models.OneToOneField(User, models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль  учителя"
        verbose_name_plural = "Профили учителей"
