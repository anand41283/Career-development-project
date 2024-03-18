from django.urls import path
from college import views

urlpatterns=[
    path('college_home/',views.CollegeHome.as_view(),name="college_home"),
]