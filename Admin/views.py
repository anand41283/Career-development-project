from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from CarrierApp.models import Student,College,Course,Login

# Create your views here.

class AdminHome(TemplateView):
    template_name='Admin_temp/index.html'

class StudentList(View):
    def get(self,request):
        data=Student.objects.all()
        return render(request,'Admin_temp/studentlist.html',{"data":data})
class StudentDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')   
        student_instance = Student.objects.get(id=id)
        user_instance = student_instance.user
        student_instance.delete()
        user_instance.delete()
        return redirect('student_list') 
    
class CollegeList(View):
    def get(self,request):
        data=College.objects.all()
        return render(request,'Admin_temp/collegelist.html',{"data":data})
class CollegeDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')   
        college_instance = College.objects.get(id=id)
        user_instance = college_instance.user

        # Delete the College instance and its associated Login instance
        college_instance.delete()
        user_instance.delete()
        return redirect('college_list')
             




