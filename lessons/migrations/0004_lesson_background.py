# Generated by Django 4.0.3 on 2022-05-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_topic_remove_lesson_status_alter_lesson_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='background',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Картинка для урока'),
        ),
    ]
