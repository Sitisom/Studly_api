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


class RatePlan(DefaultAbstractFields):
    title = models.CharField("Название тарифа", max_length=128)
    price = models.PositiveSmallIntegerField("Цена", default=0)
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", ]
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"


class Course(DefaultAbstractFields):
    title = models.CharField(max_length=128)
    teacher = models.ForeignKey(User, models.SET_NULL, "courses", null=True, verbose_name="Учитель")
    rate_plan = models.ForeignKey(RatePlan, models.SET_NULL, "courses", null=True)

    difficulty = models.ForeignKey(Difficulty, models.SET_NULL, "courses", null=True, verbose_name="Сложность")
    subject = models.ForeignKey(Subject, models.SET_NULL, "courses", null=True, verbose_name="Предмет")

    def __str__(self):
        return f'{self.title} - {self.subject}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Subscription(DefaultAbstractFields):
    user = models.ForeignKey(User, models.CASCADE, "subscriptions", null=True)
    rate_plan = models.ForeignKey(RatePlan, models.SET_NULL, "subscriptions", null=True)
    is_valid = models.BooleanField("Валидна?", default=False)

    def __str__(self):
        return f'Подписка {self.user.username} - {self.rate_plan.title}'

    class Meta:
        unique_together = ("user", "rate_plan")
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
