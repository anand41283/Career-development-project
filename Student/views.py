from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,UpdateView
from Student.forms import Stud_profileForm
from CarrierApp.models import Student,College,Course
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
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Student.objects.filter(user=id)
        return render(request,'Stud_templates/profileview.html',{"data": data})
    
class Stud_profileEdit(View):
    # template_name='Stud_templates/Add_profile.html'
    # form_class=Stud_profileForm
    # model=Student
    # success_url=reverse_lazy('Stud_home')
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Student.objects.get(user=id)
        form=Stud_profileForm(instance=data)  
        return render(request,'Stud_templates/Add_profile.html',{"form":form})  
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Student.objects.get(user=id)
        form=Stud_profileForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('Stud_home')     

class CollegeView(View):
    def get(self,request):
        data=College.objects.all()
        return render(request,'Stud_templates/CollegeView.html',{"data":data})
class CourseView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=Course.objects.filter(College_name=id)
        return render(request,'Stud_templates/CourseView.html',{"data":data})


               
    
    






