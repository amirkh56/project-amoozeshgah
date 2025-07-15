from django.db import models
from multiselectfield import MultiSelectField
from courses.models import LearningCourses
from courses.models import COURSE_GROUP
# Create your models here.

WEEK_DAYS = (
    ('0', 'Shanbe'),
    ('1', 'YekShanbe'),
    ('2', 'DoShanbe'),
    ('3', 'SeShanbe'),
    ('4', 'CharShanbe'),
    ('5', 'PanjShanbe'),
    ('6', 'Jomae'),
)

class Schedule (models.Model):
    course_name = models.OneToOneField(LearningCourses, on_delete=models.CASCADE, verbose_name="نام دوره" )
    start_date = models.DateField(verbose_name="")
    session_date = MultiSelectField(choices=WEEK_DAYS, verbose_name="روز های برگذاری")
    session_time = models.TimeField()
    enrollment_capacity = models.IntegerField(verbose_name="ظرفیت ثبت نام")
    group = models.CharField(max_length=2, choices=COURSE_GROUP, verbose_name="دسته",null=True, blank=True)

    def  __str__(self):
        return self.course_name.name

