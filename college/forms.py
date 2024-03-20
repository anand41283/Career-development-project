from django import forms
from CarrierApp.models import College,Course

class CollegeProfileForm(forms.ModelForm):
    class Meta:
        model=College
        fields=['name','place','Type','Description','cut_off_mark']


class AddCourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['Courses']  
             
    