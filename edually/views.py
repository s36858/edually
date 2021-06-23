from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from .models import Course
from .forms import *
from .tables import *


class CrispyFormMixin(object):
    """Add 'form' to the context object, allowing for the use of django crispy forms."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context["form"] = self.form_class(
            instance=object, request=self.request
        )
        return context


def index(request):
    return render(request, "edually/index.html")


def confirmation(request):
    return render(request, "edually/confirmation.html")


# course

def courseList(request):
    data = Course.objects.all()
    table = CourseTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/course/course_table.html", {"table": table})


class CourseCreateView(CreateView, CrispyFormMixin):
    model = Course
    form_class = CourseForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("course_list")


class CourseEditView(UpdateView, CrispyFormMixin):
    model = Course
    form_class = CourseForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("course_list")


class CourseDeleteView(DeleteView, CrispyFormMixin):
    model = Course

    def get_success_url(self):
        return reverse("course_list")

# semester


def semesterList(request):
    data = Semester.objects.all()
    table = SemesterTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/semester/semester_table.html", {"table": table})


class SemesterCreateView(CreateView, CrispyFormMixin):
    model = Semester
    form_class = SemesterForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("semester_list")


class SemesterEditView(UpdateView, CrispyFormMixin):
    model = Semester
    form_class = SemesterForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("semester_list")


class SemesterDeleteView(DeleteView, CrispyFormMixin):
    model = Semester

    def get_success_url(self):
        return reverse("semester_list")

# course_content


def courseContentList(request):
    data = CourseContent.objects.all()
    table = CourseContentTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/coursecontent/coursecontent_table.html", {"table": table})


class CourseContentCreateView(CreateView, CrispyFormMixin):
    model = CourseContent
    form_class = CourseContentForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("coursecontent_list")


class CourseContentEditView(UpdateView, CrispyFormMixin):
    model = CourseContent
    form_class = CourseContentForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("coursecontent_list")


class CourseContentDeleteView(DeleteView, CrispyFormMixin):
    model = CourseContent

    def get_success_url(self):
        return reverse("coursecontent_list")


# student


def studentList(request):
    data = Student.objects.all()
    table = StudentTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/student/student_table.html", {"table": table})


class StudentCreateView(CreateView, CrispyFormMixin):
    model = Student
    form_class = StudentForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("student_list")


class StudentEditView(UpdateView, CrispyFormMixin):
    model = Student
    form_class = StudentForm
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse("student_list")


class StudentDeleteView(DeleteView, CrispyFormMixin):
    model = Student

    def get_success_url(self):
        return reverse("student_list")
