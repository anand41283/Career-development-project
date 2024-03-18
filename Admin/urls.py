from django.urls import path
from Admin import views

urlpatterns=[
    path('super_home/',views.AdminHome.as_view(),name="super_home"),
]