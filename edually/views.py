from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from .models import Course
from .forms import *
from .tables import *
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect


def index(request):
    return render(request, "edually/index.html")


def confirmation(request):
    return render(request, "edually/confirmation.html")

# ----  Lists ----


def courseList(request):
    data = Course.objects.all()
    table = CourseTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/course/course_table.html", {"table": table})


def semesterList(request):
    data = Semester.objects.all()
    table = SemesterTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/semester/semester_table.html", {"table": table})


def courseContentList(request):
    data = CourseContent.objects.all()
    table = CourseContentTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/coursecontent/coursecontent_table.html", {"table": table})


def studentList(request):
    data = Student.objects.all()
    table = StudentTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/student/student_table.html", {"table": table})

# ----  Create, Edit, Delete Bases ----


class CrispyFormMixin(object):
    """Add 'form' to the context object, allowing for the use of django crispy forms."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = self.get_object()
        context["form"] = self.form_class(
            instance=object, request=self.request
        )
        return context


class BaseCreateView(CreateView, CrispyFormMixin):
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse(self.success_path)


class BaseEditView(UpdateView, CrispyFormMixin):
    template_name = "base_form.html"

    def get_success_url(self):
        return reverse(self.success_path)


class BaseDeleteView(DeleteView, CrispyFormMixin):
    def get_success_url(self):
        return reverse(self.success_path)


# ----  course ----


class CourseCreateView(BaseCreateView):
    model = Course
    form_class = CourseForm
    success_path = "course_list"


class CourseEditView(BaseEditView):
    model = Course
    form_class = CourseForm
    success_path = "course_list"


class CourseDeleteView(DeleteView, CrispyFormMixin):
    model = Course

    def get_success_url(self):
        return reverse("course_list")


# ----  semester ----


class SemesterCreateView(BaseCreateView):
    model = Semester
    form_class = SemesterForm
    success_path = "semester_list"


class SemesterEditView(BaseEditView):
    model = Semester
    form_class = SemesterForm
    success_path = "semester_list"


class SemesterDeleteView(BaseDeleteView):
    model = Semester
    success_path = "semester_list"


# ----  course_content ----


class CourseContentWizard(SessionWizardView):
    template_name = "edually/coursecontent/coursecontent_form.html"
    form_list = [CourseContentFormStep1, CourseContentFormStep2]
    model = CourseContent

    def get_form_kwargs(self, step=None):
        kwargs = {}
        if step == '1':
            course = self.get_cleaned_data_for_step('0')['course']
            obj = Course.objects.get(id=course.id)
            kwargs.update({'folder_path': obj.folder_path, })
        return kwargs

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        data_dict = form_data[1]
        data_dict['course'] = Course.objects.get(id=form_data[0]['course'].id)
        obj = CourseContent(**data_dict)
        obj.save()
        return HttpResponseRedirect('/edually/content/list')


class CourseContentEditView(BaseEditView):
    model = CourseContent
    form_class = CourseContentEditForm
    success_path = "coursecontent_list"


class CourseContentDeleteView(BaseDeleteView):
    model = CourseContent
    success_path = "coursecontent_list"


# ---- student  ----


class StudentCreateView(BaseCreateView):
    model = Student
    form_class = StudentForm
    success_path = "student_list"


class StudentEditView(BaseEditView):
    model = Student
    form_class = StudentForm
    success_path = "student_list"


class StudentDeleteView(BaseDeleteView):
    model = Student
    success_path = "student_list"


# ----  course execution ----

# def courseExecutionList(request):
#     data = CourseExecution.objects.all()
#     table = CourseExecutionTable(data)
#     RequestConfig(request).configure(table)
#     return render(request, "edually/courseexecution/courseexecution_table.html", {"table": table})


class CourseExecutionCreateView(CreateView, CrispyFormMixin):
    model = CourseExecution
    form_class = CourseExecutionForm
    template_name = "base_form.html"
    success_url = "/edually/confirmation"

    # def get_success_url(self):
    #     return reverse("student_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        self.object.create_weeks()
        return super().form_valid(form)


# class CourseExecutionView(UpdateView, CrispyFormMixin):
#     model = CourseExecution
#     form_class = StudentForm
#     template_name = "base_form.html"

#     def get_success_url(self):
#         return reverse("student_list")


# class CourseExecutionDeleteView(DeleteView, CrispyFormMixin):
#     model = CourseExecution

#     def get_success_url(self):
#         return reverse("student_list")
