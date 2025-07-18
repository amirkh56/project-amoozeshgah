# Generated by Django 5.2 on 2025-04-18 13:32

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutumnSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_start_date', models.DateField(verbose_name='تاریخ شروع')),
                ('A_session_date', multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Shanbe'), ('1', 'YekShanbe'), ('2', 'DoShanbe'), ('3', 'SeShanbe'), ('4', 'CharShanbe'), ('5', 'PanjShanbe'), ('6', 'Jomae')], max_length=13, verbose_name='روز های برگذاری')),
                ('A_session_time', models.TimeField(verbose_name='مدت زمان جلسه')),
                ('A_enrollment_capacity', models.IntegerField(verbose_name='ظرفیت ثبت نام')),
                ('A_group', models.CharField(blank=True, choices=[('1', 'all'), ('2', 'office'), ('3', 'graphic'), ('4', 'web design'), ('5', 'engineering')], max_length=2, null=True, verbose_name='دسته')),
                ('A_course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_name', to='courses.learningcourses', verbose_name='نام دوره')),
            ],
        ),
        migrations.CreateModel(
            name='WinterSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='')),
                ('session_date', multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Shanbe'), ('1', 'YekShanbe'), ('2', 'DoShanbe'), ('3', 'SeShanbe'), ('4', 'CharShanbe'), ('5', 'PanjShanbe'), ('6', 'Jomae')], max_length=13, verbose_name='روز های برگذاری')),
                ('session_time', models.TimeField()),
                ('enrollment_capacity', models.IntegerField(verbose_name='ظرفیت ثبت نام')),
                ('group', models.CharField(blank=True, choices=[('1', 'all'), ('2', 'office'), ('3', 'graphic'), ('4', 'web design'), ('5', 'engineering')], max_length=2, null=True, verbose_name='دسته')),
                ('course_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.learningcourses', verbose_name='نام دوره')),
            ],
        ),
    ]
