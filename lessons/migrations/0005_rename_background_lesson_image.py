# Generated by Django 4.0.3 on 2022-05-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_lesson_background'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='background',
            new_name='image',
        ),
    ]