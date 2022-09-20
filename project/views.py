from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, request
from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView, 
    FormView
)
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from cashflow.models import Account
from contact.models import Company
from accounts.models import User
from .models import Project
from .forms import AddProjectForm
from cashflow.models import Transaction
from .filters import ProjectFilter
from django.db.models import Sum
from .choice import PROJECT_TYPE_CHOICES, CONTRACT_TYPE_CHOICES, STATUS_TYPE_CHOICES, TRANSACTION_TYPE_CHOICES

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
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddProjectView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = User.objects.all()
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
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = User.objects.all()
        context["projects"] = Project.objects.all()
        context["projectstatus"] = STATUS_TYPE_CHOICES
        context["transactions"] = TRANSACTION_TYPE_CHOICES
        context["contracts"] = CONTRACT_TYPE_CHOICES
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        return context
   

class ProjectDeleteView(RedirectPermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Project
    template_name= "project_delete.html"
    success_message = "Product deleted successfully."
    permission_required= 'project.delete_project'
    success_url = reverse_lazy('project:projectlist')


