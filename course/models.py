from django.db import models

from core.models import User, DefaultAbstractFields


class Difficulty(models.Model):
    title = models.CharField("Название", max_length=90)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сложность курса"
        verbose_name_plural = "Сложности курсов"


class Subject(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class RatePlan(models.Model):
    title = models.CharField("Название тарифа", max_length=128)


class Course(models.Model):
    title = models.CharField(max_length=128)
    teacher = models.ForeignKey(User, models.SET_NULL, "courses", null=True, verbose_name="Учитель")
    rate_plan = models.ForeignKey(RatePlan, models.SET_NULL, "courses")

    difficulty = models.ForeignKey(Difficulty, models.SET_NULL, "courses", null=True, verbose_name="Сложность")
    subject = models.ForeignKey(Subject, models.SET_NULL, "courses", null=True, verbose_name="Предмет")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.subject}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Subscription(DefaultAbstractFields):
    user = models.ForeignKey(User, models.CASCADE, null=True)
    course = models.ForeignKey(Course, models.CASCADE, "subscriptions", null=True, )
    date = models.DateField("Дата подписки")
    is_valid = models.BooleanField("Валидна?", default=False)

    def __str__(self):
        return f'Покупка {self.user.username} - {self.course}'

    class Meta:
        unique_together = ("user", "course")
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курсы"
