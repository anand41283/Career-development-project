from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AdminHome(TemplateView):
    template_name='Admin_temp/index.html'