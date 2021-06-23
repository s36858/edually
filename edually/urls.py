from django.urls import path

from . import views

urlpatterns = [
    path('semester/delete/<pk>', views.SemesterDeleteView.as_view(),
         name="semester_delete"),
    path('semester/edit/<pk>', views.SemesterEditView.as_view(), name="semester_edit"),
    path('semester/create', views.SemesterCreateView.as_view(),
         name="semester_create"),
    path('course/delete/<pk>', views.CourseDeleteView.as_view(), name="course_delete"),
    path('course/edit/<pk>', views.CourseEditView.as_view(), name="course_edit"),
    path('course/create', views.CourseCreateView.as_view(),
         name="course_create"),
    path('semester/list', views.semesterList, name="semester_list"),
    path('course/list', views.courseList, name="course_list"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('', views.index, name='index'),
]
