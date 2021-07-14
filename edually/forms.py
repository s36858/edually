from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

COURSE_CATEGORY_CHOICES = {
    ("VO", "Vorlesung"), ("UE", 'Übung'), ("VU", "Vorlesung mit Übung")

}

LECTURE_DAYS_CHOICES = {
    ("MON", "Monday"), ("TUE", 'Tuesday'),
    ("WED", "Wednesday"), ("THU", "Thursday"),
    ("FRI", "Friday"),  ("SAT", "Saturday"), ("SUN", "Sunday")

}

COURSE_ACTION_CHOICES = {("E-Mail", "E-Mail"), ("Umfrage", "Umfrage")}


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


class CourseContentEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    class Meta:
        model = CourseContent
        fields = ("name",)


class CourseActionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    category = forms.ChoiceField(choices=COURSE_ACTION_CHOICES)

    class Meta:
        model = CourseAction
        fields = ("course", 'name', 'category', 'template')


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


class CourseWeekForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    def clean(self):
        cleaned_data = super().clean()
        add_week_to_calendar = cleaned_data.get("add_to_calendar")
        set_reminder = cleaned_data.get("reminder")
        if add_week_to_calendar:
            if set_reminder is None:
                self._errors['reminder'] = self.error_class(
                    ["Please set a reminder."])

    add_to_calendar = forms.BooleanField(
        label="Add week to calendar.", required=False)
    reminder = forms.IntegerField(
        label="Set reminder in minutes", help_text="e.g. 1 Day = 360 minutes, 1 week = 2520 minutes", required=False)

    # self.fields['course_action'].queryset = CourseAction.objects.filter(
    #     category="E-Mail")

    class Meta:
        model = CourseWeek
        fields = ('send_mail', 'send_doodle',
                  'course_action', 'course_content', "add_to_calendar", "reminder")
