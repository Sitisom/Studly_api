from django.db import models

from core.models import User


class Difficulty(models.Model):
    title = models.CharField(max_length=90, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сложность курса'
        verbose_name_plural = 'Сложности курсов'


class Subject(models.Model):
    title = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Course(models.Model):
    title = models.CharField(max_length=90, default='')

    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.subject}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class CourseSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='subscriptions')

    date = models.DateField('Дата подписки')
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f'Покупка {self.user.username} - {self.course}'

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписки на курсы'
