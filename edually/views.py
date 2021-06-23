from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from .models import Course
from .forms import *
from .tables import CourseTable, SemesterTable


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
    return render(request, "base_table.html", {"table": table})


class CourseCreateView(CreateView, CrispyFormMixin):
    model = Course
    form_class = CourseForm
    template_name = "base_form.html"
    success_url = "/edually/confirmation"


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
    return render(request, "base_table.html", {"table": table})


class SemesterCreateView(CreateView, CrispyFormMixin):
    model = Semester
    form_class = SemesterForm
    template_name = "base_form.html"
    success_url = "/edually/confirmation"


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
