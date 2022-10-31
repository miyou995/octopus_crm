from cgitb import reset
from unittest import result
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, request
from django.urls.base import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    FormView
)
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from cashflow.models import Account
from contact.models import Company
from accounts.models import User, UserQueryset
from .models import Project, Task, Teams
from .forms import AddProjectForm, AddTaskForm, AddTeamForm
from cashflow.models import Transaction
from .filters import ProjectFilter
from django.db.models import Sum
from .choice import PROJECT_TYPE_CHOICES, CONTRACT_TYPE_CHOICES, STATUS_TYPE_CHOICES, TRANSACTION_TYPE_CHOICES
from events.choice import EVENT_PRIORITY

import logging
from pprint import pprint

# Create your views here.
class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())
#project    

class ProjectListView(RedirectPermissionRequiredMixin,ListView): 
    template_name= "project_list.html"
    model = Project 
    permission_required= 'project.view_project'
    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context["project_count"] =Project.objects.all().count()
        # dettes = Project.objects.all().aggregate(Sum('get_project_dettes'))
        # print('total dettes', dettes)
        filters=ProjectFilter(self.request.GET, queryset=Project.objects.all())
        context["projects"] = filters.qs
        context["companies"] = Company.objects.all()
        context["employees"] = User.objects.all()
        context["employees_in"] = UserQueryset.is_internal_emp(self)

        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["projectstatus"] = STATUS_TYPE_CHOICES
        context["transactions"] = TRANSACTION_TYPE_CHOICES
        context["contracts"] = CONTRACT_TYPE_CHOICES
        return context
    
class ProjectDetailView(RedirectPermissionRequiredMixin,DetailView):
    model = Project
    template_name= "project_detail.html"
    permission_required= 'project.view_project'
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        project = self.get_object()
        print("sdsdddddddYTTTTTTTTTTTT: ", project)
        # project.get_project_dettes()
        project_id = self.get_object().id
        # context["project_transactions"] = Transaction.objects.filter(project=project_id)
        filters=ProjectFilter(self.request.GET, queryset=Project.objects.all())
        context["projects"] = filters.qs
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["projectstatus"] = STATUS_TYPE_CHOICES
        context["transactions"] = TRANSACTION_TYPE_CHOICES
        context["contracts"] = CONTRACT_TYPE_CHOICES
        return context
        
class AddProjectView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name= "project_add.html"
    form_class= AddProjectForm
    model = Project
    success_message = "Project added successfully."
    permission_required= 'project.add_project'
    success_url = reverse_lazy('project:projectlist')
    
    def form_valid(self,  form):
        team_list = self.request.POST.getlist('team')
        print ("sdfasdfsdfs=====: ", team_list)
        team = list(map(int,team_list))
        print(" OUR TEAM:  ",team)
        print("this project team:   ", Project.team )
        return super().form_valid( form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.as_text())
        result = redirect('project:projectlist')
        return result

    def get_context_data(self, **kwargs):
        context = super(AddProjectView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = User.objects.all()
        context["employees_in"] = UserQueryset.is_internal_emp(self)

        context["projectstatus"] = STATUS_TYPE_CHOICES
        context["transactions"] = TRANSACTION_TYPE_CHOICES
        context["contracts"] = CONTRACT_TYPE_CHOICES
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        return context

 
class ProjectUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Project
    form_class= AddProjectForm
    template_name = 'project_edit.html' 
    success_message = "Project updated successfully."
    permission_required= 'project.change_project'
    success_url = reverse_lazy('project:projectlist')
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.as_text())
        result = redirect('project:projectlist')
        return result
        # return redirect('project:projectlist')
        
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = User.objects.all()
        context["employees_in"] = UserQueryset.is_internal_emp(self)

        context["projects"] = Project.objects.all()
        context["projectstatus"] = STATUS_TYPE_CHOICES
        context["transactions"] = TRANSACTION_TYPE_CHOICES
        context["contracts"] = CONTRACT_TYPE_CHOICES
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        return context
   
# def ProjectUpdateView(request, pk):
#     if request.POST:
#         return redirect('project:projectlist')
#     # return redirect(request, 'project:projectlist')
    


class ProjectDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Project
    template_name= "project_delete.html"
    success_message = "Product deleted successfully."
    permission_required= 'project.delete_project'
    success_url = reverse_lazy('project:projectlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('project:projectlist')

######### TASKS #########


class TaskListView(RedirectPermissionRequiredMixin,SuccessMessageMixin, ListView ):
    template_name = 'task_list.html'
    model = Task
    form_class= AddTaskForm
    permission_required= 'project.list_task'
        
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        # context["employees_in"] = User.objects.all()
        context["employees_in"] = UserQueryset.is_internal_emp(self)

        context["taskpriorities"] = EVENT_PRIORITY
        context["tasks"] = Task.objects.all()

        # context["team_members"] = User.objects.filter(project_teams__isnull=False)

        # print("weeeeeeeeellllll=== ", context["team_mexmbers"])


        return context



class TaskCreateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView ):
    template_name = 'task_create_model.html'
    model = Task
    form_class= AddTaskForm
    success_message = "Task created successfully."
    permission_required= 'project.create_task'
    success_url = reverse_lazy('project:tasklist')      
        
    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context["employees_in"] = UserQueryset.is_internal_emp(self)
        context["taskpriorities"] = EVENT_PRIORITY

        context["team_members"] = Project.objects.all()
        print("weeeeeeeeellllll=== ", context["team_members"])

        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('project:tasklist')

class TaskUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView ):
    template_name = 'task_edit_model.html'
    model = Task
    form_class= AddTaskForm
    success_message = "Task updated successfully."
    permission_required= 'project.edit_task'
    success_url = reverse_lazy('project:tasklist')      
        
    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context["employees_in"] = User.objects.all()
        context["taskpriorities"] = EVENT_PRIORITY

        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('project:tasklist')


class TaskDetailView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DetailView ):
    template_name = 'task_detail.html'
    model = Task
    form_class= AddTaskForm
    permission_required= 'project.view_task'
        
    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["employees_in"] = User.objects.all()
        
        return context

        

class TaskDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView ):
    template_name = 'task_delete_model.html'
    model = Task
    form_class= AddTaskForm
    success_message = "Task deleted successfully."
    permission_required= 'project.delete_task'
    success_url = reverse_lazy('project:tasklist')      

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('project:tasklist')


###### TEAMS #######

class TeamListView(RedirectPermissionRequiredMixin, TemplateView):
    template_name = "teams_list.html"
    permission_required = "project.list_team"

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context["employees_in"] = UserQueryset.is_internal_emp(self)
        
        return context

class TeamCreateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name = "team_create_model.html"
    model = Teams
    form_class = AddTeamForm
    success_message = "Team Added successfully"
    permission_required = 'Project.add_team'
    success_url = reverse_lazy('project:teamlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been added")
        return redirect('project:teamlist')

    def form_valid(self,  form):
        team_list = self.request.POST.getlist('id_team')
        print ("sdfasdfsdfs=====: ", team_list)
        team = list(map(int,team_list))
        print(" OUR TEAM:  ",team)
        # print("this project team:   ", Project.team )
        return super().form_valid( form)

    def get_context_data(self, **kwargs):
        context = super(TeamCreateView, self).get_context_data(**kwargs)
        context["employees_in"] = UserQueryset.is_internal_emp(self)
        
        return context

class TeamUpdateView(RedirectPermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    template_name = "team_Update_model.html"
    model = Teams
    form_class = AddTeamForm
    success_message = "Team updated successfully"
    permission_required = 'Project.edit_team'
    success_url = reverse_lazy('project:teamlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been updated")
        return redirect('project:teamlist')

    def get_context_data(self, **kwargs):
        context = super(TeamUpdateView, self).get_context_data(**kwargs)
        context["employees_in"] = UserQueryset.is_internal_emp(self)
        
        return context
    
class TeamDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    template_name = "team_Delete_model.html"
    model = Teams
    form_class = AddTeamForm
    success_message = "Team Added successfully"
    permission_required = 'Project.delete_team'
    success_url = reverse_lazy('project:teamlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('project:teamlist')