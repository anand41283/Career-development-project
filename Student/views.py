from django.shortcuts import render
from django.views.generic import TemplateView,View

# Create your views here.

class StudentHome(TemplateView):
    template_name='Stud_templates/index.html'

