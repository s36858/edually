from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

COURSE_CATEGORY_CHOICES = {
    ("VO", "Vorlesung"), ("UE", 'Übung'), ("VU", "Vorlesung mit Übung")

}

LECTURE_DAYS_CHOICES = {
    ("MON", "Monday"), ("TUE", 'Tuesday'),
    ("Wed", "Wednesday"), ("THU", "Thursday"),
    ("FRI", "Friday"),  ("SAT", "Saturday"), ("SUN", "Sunday")

}


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    category = forms.ChoiceField(choices=COURSE_CATEGORY_CHOICES)

    class Meta:
        model = Course
        fields = ("name", "category", "folder_path")


class SemesterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    class Meta:
        model = Semester
        fields = ("name", "start_date", "end_date", )


class CourseContentFormStep1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    class Meta:
        model = CourseContent
        fields = ("course",)


class CourseContentFormStep2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        folder_path = kwargs.pop('folder_path', None).replace('\\', '/')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))
        self.fields["path"] = forms.FilePathField(
            path=folder_path, recursive=True
        )

    class Meta:
        model = CourseContent
        fields = ("name", "path", )


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    class Meta:
        model = Student
        fields = ("student_id", "firstname", "lastname", "email")


class CourseExecutionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    lecture_day = forms.ChoiceField(choices=LECTURE_DAYS_CHOICES)

    class Meta:
        model = CourseExecution
        fields = ("semester", "course", "lecture_day",
                  "start_time", "end_time", "enrolled_count")
