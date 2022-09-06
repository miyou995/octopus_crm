from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
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
from pprint import pprint
from contact.models import Company
from .models import  Account, Transaction
from project.models import Project
from .filters import Accountfilter, Transactionfilter
from .forms import AddAccountForm, AddTransactionForm
from django.db.models import Sum

# Create your views here.

#cashflow

    
class CashflowAccountListView(ListView): 
    template_name= "account_list.html"
    model = Account 
    def get_context_data(self, **kwargs):
        context = super(CashflowAccountListView, self).get_context_data(**kwargs)
        context["account_count"] =Account.objects.all().count()
        filters=Accountfilter(self.request.GET, queryset=Account.objects.all())
        context["accounts"] = filters.qs
        return context

class AccountDetailView(DetailView):
    model = Account
    template_name= "cashflow_account_detail.html"
    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        account_id = self.get_object().id
        context["account_transactions"] = Transaction.objects.filter(account=account_id)
        context["transactions"] = Transaction.objects.all()
        return context 

class AddAccountView(CreateView):
    template_name= "add-accounts.html"
    form_class= AddAccountForm
    model = Account
    success_url = reverse_lazy('cashflow:accountlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs): 
        context = super(AddAccountView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context
   
##### 

class CashflowListView(ListView): 
    template_name= "cashflow_list.html"
    model = Transaction 
    def get_context_data(self, **kwargs):
        context = super(CashflowListView, self).get_context_data(**kwargs)
        # context["transactions"] =Transaction.objects.all().order_by('date')
        filters=Transactionfilter(self.request.GET, queryset=Transaction.objects.all())
        context["transactions"] = filters.qs
        context["transactions_count"] =Transaction.objects.all().count()
        context["total"] =Transaction.payments.get_total()
        # context["total_dettes"] = Project.objects.all().aggregate(Sum('get_project_dettes'))
        context["total_payment"] =Transaction.payments.get_total_payment()
        context["total_charges"] =Transaction.payments.get_total_charges()
        context["total_creance"] =Transaction.payments.get_total_creance()
        context["total_salaire"] =Transaction.payments.get_total_salaire()    
        context["total_allouer"] =Transaction.payments.get_total_allouer()  
        return context


class AddTransactionView(CreateView):
    template_name= "add-transaction.html"
    form_class= AddTransactionForm
    model = Transaction
    success_url = reverse_lazy('cashflow:cashflowlist')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super(AddTransactionView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["accounts"] = Account.objects.all()
        context["projects"] = Project.objects.all()
        return context