from django.db import models

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE, null=True, related_name='teacher_profile')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль  учителя'
        verbose_name_plural = 'Профили учителей'
