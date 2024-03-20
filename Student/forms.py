from django import forms
from CarrierApp.models import Student


class Stud_profileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name', 'place', 'phone', 'age', 'Gender', 'email', 'qualification']

    