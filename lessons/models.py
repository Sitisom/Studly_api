from enum import Enum

from django.db import models

from course.models import Course


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
    title = models.CharField(max_length=128, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name='lessons')
    attachments = models.OneToOneField('LessonAttachments', on_delete=models.SET_NULL, null=True,
                                       related_name='lesson')

    status = models.CharField(max_length=20, choices=Statuses.as_choices(), default=Statuses.UNDONE.value)

    def __str__(self):
        return f'{self.title} - {self.course.title} - {self.course.subject}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Task(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, related_name='tasks')

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
        return 'Вариант к заданию %s (%s)' % (self.task, self.text)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Assignment(models.Model):
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Учитель')
    student = models.ForeignKey('students.Student', on_delete=models.SET_NULL, null=True, verbose_name='Студент')
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, related_name='lesson_assignment',
                               verbose_name='Урок')

    status = models.CharField(choices=Statuses.as_choices(), default=Statuses.UNDONE.value,
                              max_length=120, verbose_name='Статус')

    def __str__(self):
        return 'Тест %s для ученика %s' % (self.lesson, self.student)

    class Meta:
        verbose_name = 'Назначение тестов'
        verbose_name_plural = 'Назначения тестов'


class TaskAnswer(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, null=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True,
                             related_name='answers')
    answer = models.TextField(null=True)
    points = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Ответ на задание'
        verbose_name_plural = 'Ответы на задание'


class LessonAttachments(models.Model):
    text = models.TextField(null=True)
    file = models.FileField(null=True, upload_to='attachments/files/')
    video_url = models.URLField(null=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Дополнение к тесту'
        verbose_name_plural = 'Дополнения к тесту'
