# Generated by Django 5.1.3 on 2025-06-16 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_learningcourses_image_learningcourses_is_active_and_more'),
        ('learningcalenders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WinterSchedule',
            new_name='Schedule',
        ),
        migrations.DeleteModel(
            name='AutumnSchedule',
        ),
    ]
