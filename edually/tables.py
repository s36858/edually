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


class CourseContentTable(tables.Table):
    class Meta:
        model = CourseContent
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("id", "course", "name", "get_filename")

    get_filename = tables.columns.Column(verbose_name="Filename")

    edit = TemplateColumn(
        template_name="edually/coursecontent/coursecontent_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/coursecontent/coursecontent_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class CourseActionTable(tables.Table):
    class Meta:
        model = CourseAction
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        exclude = []

    edit = TemplateColumn(
        template_name="edually/courseaction/courseaction_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/courseaction/courseaction_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class StudentTable(tables.Table):
    class Meta:
        model = Student
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("student_id", "firstname", "lastname", "email")

    edit = TemplateColumn(
        template_name="edually/student/student_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/student/student_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class SemesterOverviewTable(tables.Table):
    class Meta:
        model = Semester
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("id", "name", "start_date", "end_date")

    show = TemplateColumn(
        template_name="edually/semester/semester_show_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class CourseExecutionTable(tables.Table):
    class Meta:
        model = CourseExecution
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        exclude = []

    weeks = TemplateColumn(
        template_name="edually/courseweek/courseweek_show_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    edit = TemplateColumn(
        template_name="edually/courseexecution/courseexecution_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    delete = TemplateColumn(
        template_name="edually/courseexecution/courseexecution_delete_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )


class CourseWeekTable(tables.Table):
    class Meta:
        model = CourseWeek
        attrs = {"class": settings.EDUALLYDESIGN["table"]["table"]}
        fields = ("get_semester", "week", "week_date",
                  "send_mail", "send_doodle", "notes", "state")

    get_semester = tables.columns.Column(verbose_name="Semester")

    edit = TemplateColumn(
        template_name="edually/courseweek/courseweek_edit_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )

    detail = TemplateColumn(
        template_name="edually/courseweek/courseweek_detail_column.html",
        extra_context={"eduallydesign": settings.EDUALLYDESIGN, }, orderable=False
    )
