from enum import Enum

from django.db import models

from course.models import Course
from students.models import Student


class Statuses(Enum):
    UNDONE = 'UNDONE'
    DONE = 'DONE'

    @classmethod
    def as_choices(cls):
        return (
            (cls.UNDONE.value, "Не закончил"),
            (cls.DONE.value, "Закончил")
        )


class Lesson(models.Model):
    title = models.CharField("Название", max_length=128, default='')
    course = models.ForeignKey(Course, models.CASCADE, "lessons", null=True)

    status = models.CharField("Статус", max_length=20, choices=Statuses.as_choices(), default=Statuses.UNDONE.value)

    def __str__(self):
        return f'{self.title} - {self.course.title} - {self.course.subject}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class TaskType(Enum):
    TEST = "TEST"
    TEXT = "TEXT"

    @classmethod
    def as_choices(cls):
        return (
            (cls.TEST.value, "Тестовое"),
            (cls.TEXT.value, "Текстовое")
        )


class Variant(models.Model):
    text = models.CharField("Текст", max_length=150, null=True)

    def __str__(self):
        return f"Вариант {self.id} ({self.text[:20]})"

    class Meta:
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"


class TaskVariantThroughModel(models.Model):
    task = models.ForeignKey("Task", models.CASCADE, )
    variant = models.ForeignKey(Variant, models.CASCADE)
    is_right = models.BooleanField(default=False)


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, models.SET_NULL, "tasks", null=True)
    question = models.CharField("Вопрос", max_length=300)
    type = models.CharField("Тип задания", choices=TaskType.as_choices())

    variants = models.ManyToManyField(Variant, through=TaskVariantThroughModel)

    def __str__(self):
        return f"Задание №{self.id}, для урока {self.lesson.id}"

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Assignment(models.Model):
    student = models.ForeignKey(Student, models.SET_NULL, null=True, verbose_name='Студент')
    lesson = models.ForeignKey(Lesson, models.CASCADE, "assignments", verbose_name='Урок')

    status = models.CharField("Статус", choices=Statuses.as_choices(), default=Statuses.UNDONE.value, max_length=120)

    def __str__(self):
        return 'Тест %s для ученика %s' % (self.lesson, self.student)

    class Meta:
        verbose_name = "Назначение задания"
        verbose_name_plural = "Назначения заданий"


class TaskAnswer(models.Model):
    student = models.ForeignKey(Student, models.CASCADE, null=True, verbose_name="Студент")
    task = models.ForeignKey(Task, models.CASCADE, "answers", null=True, verbose_name="Задача")
    answer = models.TextField("Ответ")
    points = models.FloatField("Количество баллов", default=0)

    class Meta:
        verbose_name = "Ответ на задание"
        verbose_name_plural = "Ответы на задание"


class LessonAttachments(models.Model):
    lesson = models.ForeignKey(Lesson, models.CASCADE, "attachments", verbose_name="Урок")
    text = models.TextField("Текст", null=True)
    file = models.FileField("Файл", null=True, upload_to="attachments/files/")
    video_url = models.URLField("Ссылка на видео", null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Дополнение к тесту"
        verbose_name_plural = "Дополнения к тесту"
