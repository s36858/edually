from django_tables2 import tables, TemplateColumn
from .models import *
from django.conf import settings


class CourseTable(tables.Table):
    class Meta:
        model = Course
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("id", "name", "category")

    edit = TemplateColumn(
        template_name="edually/course/course_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/course/course_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class SemesterTable(tables.Table):
    class Meta:
        model = Semester
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("id", "name", "start_date", "end_date")

    edit = TemplateColumn(
        template_name="edually/semester/semester_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/semester/semester_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )
