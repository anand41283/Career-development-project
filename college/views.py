from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from college.forms import CollegeProfileForm,AddCourseForm
from django.urls import reverse_lazy
from CarrierApp.models import College,Course
# Create your views here.

class CollegeHome(TemplateView):
    template_name='college_temp/index.html'

class CollegeProfileAdd(LoginRequiredMixin,CreateView):
    template_name='college_temp/Add_CollegeProfile.html'   
    form_class=CollegeProfileForm
    model=College
    success_url=reverse_lazy('college_home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class AddCourse(CreateView):
    template_name='college_temp/Add_course.html'
    form_class=AddCourseForm
    model=Course
    success_url=reverse_lazy('college_home')

    def form_valid(self, form):
        form.instance.College_name=self.request.user.college_profile
        return super().form_valid(form)
