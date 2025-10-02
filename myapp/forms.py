from django import forms
from django.contrib.auth.models import User
from .models import  Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','completed']
        widgets={
            'completed':forms.CheckboxInput()#to show checkbox in form
        }