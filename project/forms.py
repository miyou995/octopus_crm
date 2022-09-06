from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import Project

class AddProjectForm(ModelForm) :
    class Meta: 
        model = Project
        fields = '__all__' 
     
