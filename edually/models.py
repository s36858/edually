import datetime
import os
from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition
from django.utils import timezone
from dateutil import rrule

LECTURE_DAYS_WEEK_NR = {'MON': 0, 'TUE': 1, 'FRI': 4,
                        'WED': 2, 'THU': 3, 'SUN': 6, 'SAT': 5}


class Semester(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    folder_path = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name + " (" + self.category + ")"


class CourseContent(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    path = models.FilePathField(
        path="./content", recursive=True)

    def get_filename(self):
        return str(os.path.basename(self.path))

    def __str__(self):
        return str(self.name)


class CourseAction(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    course = models.ForeignKey(Course,  on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    template = models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)

    def get_category_by_mail(self):
        return self.objects.filter(category="E-Mail")


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()


class CourseExecution(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    enrolled_count = models.IntegerField(null=True, blank=True)
    student = models.ManyToManyField(Student)

    __original_lecture_day = None

    class Meta:
        unique_together = ['semester', 'course']

    def next_weekday(self, start_date):
        week_number = LECTURE_DAYS_WEEK_NR[self.lecture_day]
        days_ahead = week_number - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + datetime.timedelta(days_ahead)

    def get_week_dates(self):
        start_date = self.semester.start_date
        end_date = self.semester.end_date
        next_date = self.next_weekday(start_date)
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=next_date, until=end_date)
        return weeks

    def create_weeks(self):
        weeks = self.get_week_dates()
        week_count = 1
        for w in weeks:
            courseweek_obj = CourseWeek.objects.create(
                courseExecution_id=self, week=week_count, week_date=w)
            courseweek_obj.save()
            week_count = week_count+1

    def __init__(self, *args, **kwargs):
        super(CourseExecution, self).__init__(*args, **kwargs)
        self.__original_lecture_day = self.lecture_day

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.lecture_day != self.__original_lecture_day:
            weeks = self.get_week_dates()
            course_week_objects = CourseWeek.objects.filter(
                courseExecution_id=self.id)
            for date, course_week in zip(weeks, course_week_objects):
                course_week.update_date(date)

        super(CourseExecution, self).save(
            force_insert, force_update, *args, **kwargs)
        self.__original_lecture_day = self.lecture_day


class CourseWeek(models.Model):
    courseExecution_id = models.ForeignKey(
        CourseExecution, on_delete=models.CASCADE)
    week = models.IntegerField()
    week_date = models.DateField(default=timezone.now)
    send_mail = models.BooleanField(default=False)
    send_doodle = models.BooleanField(default=False)
    course_content = models.ManyToManyField(
        CourseContent, blank=True)
    course_action = models.ManyToManyField(CourseAction, blank=True)
    notes = models.TextField(blank=True, null=True, max_length=300)
    state = FSMField(default="new")

    class Meta:
        unique_together = ['courseExecution_id', 'week']

    def get_semester(self):
        return str(self.courseExecution_id.semester.name)

    def update_date(self, date):
        self.week_date = date
        self.save()
