import re
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import Project, Task, Teams
from accounts.models import UserQueryset, User

class AddProjectForm(ModelForm) :
    class Meta: 
        model = Project
        fields = '__all__' 
        
    # team=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    

class AddTaskForm(ModelForm) :
    class Meta: 
        model = Task
        fields = '__all__' 

class AddTeamForm(ModelForm) :
    # member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),queryset=UserQueryset.is_internal_empl, required=False )
    user_id = forms.CharField()
    class Meta: 
        model = Teams
        fields = '__all__' 

    # member = forms.ModelMultipleChoiceField(
    #             queryset=User.objects.filter(is_internal= True),
    #             widget=forms.CheckboxSelectMultiple(attrs={'class':'class_team'}))

        # widgets = {
        
        #     'member' : forms.ModelMultipleChoiceField(
        #                 queryset=UserQueryset.is_internal_empl,
        #                 widget=forms.CheckboxSelectMultiple)
        # }

    
 