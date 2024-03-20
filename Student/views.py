from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView
from Student.forms import Stud_profileForm
from CarrierApp.models import Student
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class StudentHome(TemplateView):
    template_name='Stud_templates/index.html'

class Stud_AddProfile(LoginRequiredMixin,CreateView):
    template_name='Stud_templates/Add_profile.html'
    form_class=Stud_profileForm
    model=Student
    success_url=reverse_lazy('Stud_home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
        
class Stud_profileView(View):
    def get(self,request):
        return render(request,'Stud_templates/profileview.html')        
    
    






