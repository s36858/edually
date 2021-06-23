from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

COURSE_CATEGORY_CHOICES = {
    ("VO", "Vorlesung"), ("UE", 'Übung'), ("VU", "Vorlesung mit Übung")

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
        fields = ("name", "category")


class SemesterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "OK"))

    class Meta:
        model = Semester
        fields = ("name", "start_date", "end_date", )
