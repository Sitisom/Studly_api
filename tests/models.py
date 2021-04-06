from enum import Enum

from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Task(models.Model):
    test = models.ForeignKey('Test', on_delete=models.SET_NULL, null=True, related_name='tasks')

    question = models.CharField(max_length=300, null=True)
    right_answer = models.TextField(null=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Variant(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, related_name='variants')
    text = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class AssignmentStatuses(Enum):
    UNDONE = 'UNDONE'
    DONE = 'DONE'
    CHECKED_BY_TEACHER = 'CHECKED_BY_TEACHER'

    @classmethod
    def as_choices(cls):
        return (
            (cls.UNDONE.value, "Не сдано"),
            (cls.DONE.value, "Сдано"),
            (cls.CHECKED_BY_TEACHER.value, "Проверено учителем")
        )


class Assignment(models.Model):
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Учитель')
    student = models.ForeignKey('students.Student', on_delete=models.SET_NULL, null=True, verbose_name='Студент')
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, null=True, related_name='test_assignment',
                             verbose_name='Тест')

    status = models.CharField(choices=AssignmentStatuses.as_choices(), default=AssignmentStatuses.UNDONE.value,
                              max_length=120, verbose_name='Статус')

    class Meta:
        verbose_name = 'Назначение тестов'
        verbose_name_plural = 'Назначения тестов'


class TaskAnswer(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    answer = models.TextField(null=True)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Ответ на задание'
        verbose_name_plural = 'Ответы на задание'


class TestAttachments(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE, null=True, related_name='attachments')

    text = models.TextField(null=True)
    file = models.FileField(null=True)
    video_url = models.URLField(null=True)

    class Meta:
        verbose_name = 'Дополнение к тесту'
        verbose_name_plural = 'Дополнения к тесту'
