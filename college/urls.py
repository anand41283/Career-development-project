from django.urls import path
from college import views

urlpatterns=[
    path('college_home/',views.CollegeHome.as_view(),name="college_home"),
    path('college_profileadd/',views.CollegeProfileAdd.as_view(),name="college_ProfileAdd"),
    path('college_courseadd/',views.AddCourse.as_view(),name="course_Add"),
]