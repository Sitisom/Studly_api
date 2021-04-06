from django.db import models

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE, null=True, related_name='student_profile')

    def __str__(self):
        return self.user.username
