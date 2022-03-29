# Generated by Django 4.0.3 on 2022-03-27 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(limit_choices_to={'role': 'STUDENT'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(limit_choices_to={'role': 'STUDENT'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Студент'),
        ),
    ]
