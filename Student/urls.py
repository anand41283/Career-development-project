from django.urls import path
from Student import views


urlpatterns=[
    path('Studenthome/',views.StudentHome.as_view(),name='Stud_home'),
]