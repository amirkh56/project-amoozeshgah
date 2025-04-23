from django.db import models

# Create your models here.
COURSE_GROUP = (
    ('1', 'all'),
    ('2', 'office'),
    ('3', 'graphic'),
    ('4', 'web design'),
    ('5', 'engineering'),
)

class LearningCourses (models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دوره")
    teacher_name = models.CharField(max_length=40,verbose_name="نام مدرس")
    teacher_family = models.CharField(max_length=50,verbose_name="نام خانوادگی مدرس",)
    teacher_licence = models.CharField(max_length=30, verbose_name="مدرک مدرس")
    desciption = models.TextField(verbose_name="توضیحات")
    number_of_sessions = models.IntegerField(verbose_name="تعداد جلسات")
    price = models.IntegerField(verbose_name="شهریه")
    group = models.CharField(choices=COURSE_GROUP, max_length=2, verbose_name="دسته",)

    def  __str__(self):
        return self.name



class LearningWorkshops (models.Model):
    workshop_name = models.CharField(max_length=50, verbose_name="نام کارگاه")
    teacher_name = models.CharField(max_length=40,verbose_name="نام مدرس")
    teacher_family = models.CharField(max_length=50,verbose_name="نام خانوادگی مدرس")
    teacher_licence = models.CharField(max_length=30, verbose_name="مدرک مدرس")
    people = models.CharField(max_length=10, verbose_name="مخاطبین")
    workshop_price = models.IntegerField(verbose_name="شهریه")
        
