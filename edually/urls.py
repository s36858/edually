from django.urls import path

from . import views


urlpatterns = [
    # course week
    path('course/week/detail/<pk>', views.CourseWeekDetailView.as_view(),
         name="course_week_detail"),
    path('course/week/edit/<pk>', views.CourseWeekEditView.as_view(),
         name="course_week_edit"),
    # course execution
    path('course/execution/delete/<pk>', views.CourseExecutionDeleteView.as_view(),
         name="course_execution_delete"),
    path('course/execution/edit/<pk>', views.CourseExecutionEditView.as_view(),
         name="course_execution_edit"),
    path('course/execution/create', views.CourseExecutionCreateView.as_view(),
         name="course_execution_create"),
    # student
    path('student/delete/<pk>', views.StudentDeleteView.as_view(),
         name="student_delete"),
    path('student/edit/<pk>', views.StudentEditView.as_view(),
         name="student_edit"),
    path('student/create', views.StudentCreateView.as_view(),
         name="student_create"),
    # action
    path('action/delete/<pk>', views.CourseActionDeleteView.as_view(),
         name="courseaction_delete"),
    path('action/edit/<pk>', views.CourseActionEditView.as_view(),
         name="courseaction_edit"),
    path('action/create', views.CourseActionCreateView.as_view(),
         name="courseaction_create"),
    # content
    path('content/delete/<pk>', views.CourseContentDeleteView.as_view(),
         name="coursecontent_delete"),
    path('content/edit/<pk>', views.CourseContentEditView.as_view(),
         name="coursecontent_edit"),
    path('content/create', views.CourseContentWizard.as_view(),
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
    path('course/create', views.CourseCreateView.as_view(), name="course_create"),
    # tables
    path('course/week/list/<pk>', views.courseWeekList,
         name="course_week_list"),
    path('course/execution/list/<pk>', views.courseExecutionList,
         name="course_execution_list"),
    path('course/execution/semester/list',
         views.semesterOverviewList, name="semester_overview_list"),
    path('student/list', views.studentList, name="student_list"),
    path('action/list', views.courseActionList, name="courseaction_list"),
    path('content/list', views.courseContentList, name="coursecontent_list"),
    path('semester/list', views.semesterList, name="semester_list"),
    path('course/list', views.courseList, name="course_list"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('', views.index, name='index'),
]
