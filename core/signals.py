from django.db.models.signals import post_save, pre_save

from core.models import Rating
from students.models import StudentProfile
from teachers.models import TeacherProfile


def user_pre_save(sender, instance, raw, created, **kwargs):
    pass


def user_post_save(sender, instance, raw, created, **kwargs):
    if created:
        if instance.is_teacher:
            TeacherProfile.objects.get_or_create(user=instance)
        elif instance.is_student:
            StudentProfile.objects.get_or_create(user=instance)
            Rating.objects.get_or_create(user=instance)


pre_save.connect(user_pre_save, "core.User")
post_save.connect(user_post_save, "core.User")
