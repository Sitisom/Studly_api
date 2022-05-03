from django.db import models

from core.models import User, DefaultAbstractFields
from core.roles import Role


class Subject(DefaultAbstractFields):
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
    title = models.CharField("Название", max_length=128)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField("Картинка", blank=True)
    teacher = models.ForeignKey(User, models.SET_NULL, "courses", null=True, verbose_name="Учитель")
    rate_plan = models.ForeignKey(RatePlan, models.SET_NULL, "courses", null=True, verbose_name="Тариф")

    difficulty = models.PositiveSmallIntegerField("Сложность", default=1, help_text="От 1 до 3")
    subject = models.ForeignKey(Subject, models.SET_NULL, "courses", null=True, verbose_name="Предмет")

    def __str__(self):
        return f'{self.title} - {self.subject}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class CourseSubscription(DefaultAbstractFields):
    user = models.ForeignKey(User, models.CASCADE, 'student_courses', limit_choices_to={'role': Role.STUDENT.value},
                             verbose_name="Пользователь")
    course = models.ForeignKey(Course, models.CASCADE, 'courses', verbose_name="Курс")

    class Meta:
        verbose_name = "Подписка на курс"
        verbose_name_plural = "Подписки на курсы"


class SubscriptionQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True, is_valid=True)


class Subscription(DefaultAbstractFields):
    user = models.ForeignKey(User, models.CASCADE, 'subscriptions', null=True, verbose_name="Пользователь")
    rate_plan = models.ForeignKey(RatePlan, models.SET_NULL, "subscriptions", null=True, verbose_name="Тариф")
    is_valid = models.BooleanField("Валидна?", default=False)

    def __str__(self):
        return f'Подписка {self.user.username} - {self.rate_plan.title}'

    class Meta:
        unique_together = ("user", 'is_active')
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
