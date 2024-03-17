from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,CreateView,FormView
from CarrierApp.forms import Registration,LoginForm
from CarrierApp.models import Login
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class Home(TemplateView):
    template_name='index.html'

# class UserRegistration(View):
#     def get(self,request):
#         form=Registration()
#         return render(request,'UserRegistration.html',{"form":form})

class UserRegistration(FormView):
    template_name='UserRegistration.html'
    form_class=Registration
    def post(self,request):
        form=Registration(request.POST)
        if form.is_valid():
            Login.objects.create_user(**form.cleaned_data)
        else:
            print("invalid")
        return redirect('login')        
            

class LoginView(FormView):
    template_name='login.html'
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(request,username=username, password=password)
            print(user)
            if user:
                login(request, user)
                if request.user.is_student:
                    return redirect('Stud_home')
                else:
                    return redirect('home')
            else:
                # Handle invalid credentials
                print("invalid")
                return redirect('login')  # Redirect back to login page with a message or something
        else:
            # Handle form validation errors
            return redirect('login')       

      


