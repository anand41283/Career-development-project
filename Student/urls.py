from django.urls import path
from Student import views


urlpatterns=[
    path('Studenthome/',views.StudentHome.as_view(),name='Stud_home'),
    path('Student_profile/',views.Stud_AddProfile.as_view(),name='Stud_Aprofile'),
    path('profile_view/',views.Stud_profileView.as_view(),name='profile_view'),
]