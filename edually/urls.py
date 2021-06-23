from django.urls import path

from . import views

urlpatterns = [
    # student
    path('student/delete/<pk>', views.StudentDeleteView.as_view(),
         name="student_delete"),
    path('student/edit/<pk>', views.StudentEditView.as_view(),
         name="student_edit"),
    path('student/create', views.StudentCreateView.as_view(),
         name="student_create"),
    # content
    path('content/delete/<pk>', views.CourseContentDeleteView.as_view(),
         name="coursecontent_delete"),
    path('content/edit/<pk>', views.CourseContentEditView.as_view(),
         name="coursecontent_edit"),
    path('content/create', views.CourseContentCreateView.as_view(),
         name="coursecontent_create"),
    # semester
    path('semester/delete/<pk>', views.SemesterDeleteView.as_view(),
         name="semester_delete"),
    path('semester/edit/<pk>', views.SemesterEditView.as_view(), name="semester_edit"),
    path('semester/create', views.SemesterCreateView.as_view(),
         name="semester_create"),
    # course
    path('course/delete/<pk>', views.CourseDeleteView.as_view(), name="course_delete"),
    path('course/edit/<pk>', views.CourseEditView.as_view(), name="course_edit"),
    path('course/create', views.CourseCreateView.as_view(),
         name="course_create"),
    # tables
    path('student/list', views.studentList, name="student_list"),
    path('content/list', views.courseContentList, name="coursecontent_list"),
    path('semester/list', views.semesterList, name="semester_list"),
    path('course/list', views.courseList, name="course_list"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('', views.index, name='index'),
]
