import re
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import Project, Task

class AddProjectForm(ModelForm) :
    class Meta: 
        model = Project
        fields = '__all__' 
        
    # team=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    

class AddTaskForm(ModelForm) :
    class Meta: 
        model = Task
        fields = '__all__' 
 