import os
from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition


class Semester(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " (" + self.category + ")"


class CourseContent(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    path = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)


class CourseAction(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    course = models.ForeignKey(Course,  on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)  # email / doodle
    template = models.TextField(max_length=300)


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

    class Meta:
        unique_together = ['semester', 'course']


class CourseWeek(models.Model):
    courseExecution_id = models.ForeignKey(
        CourseExecution, on_delete=models.CASCADE)
    week = models.IntegerField()
    send_mail = models.BooleanField(default=False)
    send_doodle = models.BooleanField(default=False)
    course_content = models.ManyToManyField(
        CourseContent)
    course_action = models.ManyToManyField(CourseAction)
    notes = models.TextField(blank=True, null=True, max_length=300)
    state = FSMField(default="new")  # email #done

    class Meta:
        unique_together = ['courseExecution_id', 'week']
