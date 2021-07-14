from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django_tables2 import RequestConfig
from .models import Course
from .forms import *
from .tables import *
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict


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


def courseActionList(request):
    data = CourseAction.objects.all()
    table = CourseActionTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/courseaction/courseaction_table.html", {"table": table})


def studentList(request):
    data = Student.objects.all()
    table = StudentTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/student/student_table.html", {"table": table})


def semesterOverviewList(request):
    data = Semester.objects.all()
    table = SemesterOverviewTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/semester/semester_table.html", {"table": table})


def courseExecutionList(request, pk):
    data = CourseExecution.objects.filter(semester=pk)
    table = CourseExecutionTable(data)
    RequestConfig(request).configure(table)
    return render(request, "edually/courseexecution/courseexecution_table.html", {"table": table})


def courseWeekList(request, pk):
    data = CourseWeek.objects.filter(courseExecution_id=pk)
    table = CourseWeekTable(data)
    semester = data.first().get_semester()
    course = data.first().courseExecution_id.course
    RequestConfig(request).configure(table)
    return render(request, "edually/courseweek/courseweek_table.html", {"table": table, "semester": semester, "course": course})

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

# ----  course_action ----


class CourseActionCreateView(BaseCreateView):
    model = CourseAction
    form_class = CourseActionForm
    success_path = "courseaction_list"


class CourseActionEditView(BaseEditView):
    model = CourseAction
    form_class = CourseActionForm
    success_path = "courseaction_list"


class CourseActionDeleteView(BaseDeleteView):
    model = CourseAction
    success_path = "courseaction_list"


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


class CourseExecutionCreateView(BaseCreateView):
    model = CourseExecution
    form_class = CourseExecutionForm

    def get_success_url(self, **kwargs):
        return reverse("course_execution_list", kwargs={'pk': self.object.semester.id})

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        self.object.create_weeks()
        return super().form_valid(form)


class CourseExecutionEditView(BaseEditView):
    model = CourseExecution
    form_class = CourseExecutionForm

    def get_success_url(self, **kwargs):
        return reverse("course_execution_list", kwargs={'pk': self.object.semester.id})


class CourseExecutionDeleteView(BaseDeleteView):
    model = CourseExecution
    success_path = "confirmation"


# ----  course week ----


class CourseWeekEditView(BaseEditView):
    model = CourseWeek
    form_class = CourseWeekForm
    template_name = "edually/courseweek/courseweek_form.html"

    def get_success_url(self, **kwargs):
        return reverse('course_week_edit', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super(CourseWeekEditView, self).get_form_kwargs()
        obj = CourseWeek.objects.get(id=self.kwargs['pk'])
        course = obj.courseExecution_id.course.id
        kwargs['course'] = course
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = CourseWeek.objects.get(id=self.kwargs['pk'])
        next_week = obj.week + 1
        try:
            obj_next_week = CourseWeek.objects.get(
                courseExecution_id=obj.courseExecution_id, week=next_week)
            context['next_week'] = obj_next_week
        except CourseWeek.DoesNotExist:
            context['next_week'] = None
        return context

    def form_valid(self, form):
        self.object = form.save()
        if self.object.add_to_calendar:
            self.object.add_to_google_calendar()
        return super().form_valid(form)


class CourseWeekDetailView(DetailView):
    model = CourseWeek
    template_name = "edually/courseweek/courseweek_detail.html"

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk:
            queryset = queryset.filter(pk=pk)
        else:
            raise AttributeError(
                "View %s must be called with a "
                "pk in the URLconf." % self.__class__.__name__
            )
        obj = queryset.get()
        record_dict = model_to_dict(obj)
        clean_record_dict = {}
        for key, value in record_dict.items():
            key = key.replace("_", " ").capitalize()
            clean_record_dict[key] = value
        return clean_record_dict
