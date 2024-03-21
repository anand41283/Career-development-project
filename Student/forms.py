from django import forms
from CarrierApp.models import Student


class Stud_profileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name', 'place', 'phone', 'age', 'Gender', 'email', 'qualification']
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Full name"}),
            "place":forms.TextInput(attrs={"class":"form-control","placeholder":"Place"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone"}),
            "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Age"}),
            "Gender": forms.Select(attrs={"class": "form-select"}),  
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder":"Email"}),  
            "qualification": forms.TextInput(attrs={"class": "form-control","placeholder":"Qualification"}),
        }
        

    