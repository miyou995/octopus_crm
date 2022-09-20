from multiprocessing import context
from pipes import Template
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls.base import reverse_lazy
from .models import Company
from project.models import Project
from accounts.models import User
from accounts.choice import ROLE_TYPE_CHOICE, DECISION_TYPE_CHOICES, PROJECT_TYPE_CHOICES
from contact.choice import COMPANY_TYPE_CHOICES

from .forms import CompanyAddForm , AddClientForm
from django.contrib import messages
from .filters import CompanyFilter, Userfilter
from pprint import pprint


class RedirectPermissionRequiredMixin(PermissionRequiredMixin):
    login_url = reverse_lazy("core:index")
    def handle_no_permission(self):
        return redirect(self.get_login_url)


class CompanyAddView(RedirectPermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'company_add.html'
    model: Company
    form_class = CompanyAddForm
    success_message = "Company created successfully"
    success_url = reverse_lazy("contact:companylist")
    permission_required = "contact.add_company"
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CompanyAddView, self).get_context_data(**kwargs)
        context["employees"] = User.objects.all()
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["companytypes"] = COMPANY_TYPE_CHOICES

        return context

class CompanyUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Company
    form_class = CompanyAddForm
    template_name = 'modal_company_edit.html'
    success_message = "Company updated successfully"
    success_url = reverse_lazy('contact:companylist')
    permission_required = "contact.update_company"

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["companytypes"] = COMPANY_TYPE_CHOICES
        context["employees"] = User.objects.all()



    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('contact:editcompany')


        # print(form.errors)
        # return super().form_invalid(form)


class CompanyDetailView(RedirectPermissionRequiredMixin, DetailView):
    model = Company
    template_name = "company_detail.html"
    permission_required= 'company.detail_company'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        company_id = self.get_object().id
        context["company_projects"] = Project.objects.filter(company = company_id)
        context["projects"] = Project.objects.all()
        context["employees"] = User.objects.all()
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["companytypes"] = COMPANY_TYPE_CHOICES
        return context

class CompanyListView(RedirectPermissionRequiredMixin, ListView):
    model = Company
    template_name = 'company_list.html'
    permission_required ='company.list_company'
    
    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        filters= CompanyFilter(self.request.GET, queryset=Company.objects.all().order_by('collab_start'))
        context["company_count"] = Company.objects.all().count()
        context["companies"] = filters.qs
        context["projecttypes"] = PROJECT_TYPE_CHOICES
        context["companytypes"] = COMPANY_TYPE_CHOICES
        context["employees"] = User.objects.all()



        return context

class CompanyDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Company
    template_name= "company_delete.html"
    permission_required= 'company.delete_company'
    success_message = "Company deleted successfully."
    success_url = reverse_lazy('contact:companylist')

    def invalid_delete(self):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")


##### CLIENTS

class  AddClientView(RedirectPermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name= "client_add.html"
    form_class= AddClientForm
    model = User

    success_message = "the employee created successfully."
    permission_required= 'contact.add_client'
    success_url = reverse_lazy('contact:clientlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('contact:clientlist')

    def get_context_data(self, **kwargs):
        context = super(AddClientView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["projects"] = Project.objects.all()
        context["roles"] = ROLE_TYPE_CHOICE
        context["decisions"] = DECISION_TYPE_CHOICES

        return context 



class ClientListView(RedirectPermissionRequiredMixin, ListView): 
    template_name= "client_list.html"
    model = User 
    permission_required= 'contact.view_client'
    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        # context["Users"] =User.objects.all().order_by('collab_start')
        context["client_count"] =User.objects.all().count()
        filters=Userfilter(self.request.GET, queryset=User.objects.all().order_by('collab_start'))
        # context["employees"] = User.objects.all()
        context["employees"] = filters.qs
        context["companies"] = Company.objects.all()
        context["projects"] = Project.objects.all()
        context["projecttypes"] = PROJECT_TYPE_CHOICES

        return context


class ClientUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class= AddClientForm
    template_name = 'client_edit.html' 
    permission_required= 'contact.change_Cclient'
    success_message = "Client updated successfully."
    success_url = reverse_lazy('contact:clientlist')


    def get_context_data(self, **kwargs):
        context = super(ClientUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('contact:clientlist')
    
class ClientDetailView(RedirectPermissionRequiredMixin, DetailView):
    model = User
    template_name= "client_detail.html"
    permission_required= 'contact.view_client'
    def get_context_data(self, **kwargs):
        context = super(ClientDetailView, self).get_context_data(**kwargs)
        User_id = self.get_object().id
        context["projects"] = Project.objects.all()
        context["employees"] = User.objects.all()
        context["companies"] = Company.objects.all()
        context["client_projects"] = Project.objects.filter(manager=User_id)
        return context

class ClientDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name= "client_delete.html"
    permission_required= 'client.delete_company'
    success_message = "Client deleted successfully."
    success_url = reverse_lazy('contact:clientlist')
