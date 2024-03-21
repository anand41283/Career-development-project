from django.urls import path
from Admin import views

urlpatterns=[
    path('super_home/',views.AdminHome.as_view(),name="super_home"),
    path('student_list/',views.StudentList.as_view(),name="student_list"),
    path('student_delete/<int:pk>/',views.StudentDelete.as_view(),name="student_delete"),
    path('college_list/',views.CollegeList.as_view(),name="college_list"),
    path('college_delete/<int:pk>/',views.CollegeDelete.as_view(),name="college_delete"),

]