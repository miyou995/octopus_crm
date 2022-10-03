from asyncio.locks import _ContextManagerMixin
from multiprocessing import context
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
from django.contrib.auth.mixins import PermissionRequiredMixin
from pprint import pprint
from bills.views import RedirectPermissionRequiredMixin
from contact.models import Company
from .models import  Account, Transaction, TransactionManager
# from project.models import Project
from .filters import Accountfilter, Transactionfilter
from .forms import AddAccountForm, TransactionCreateForm
from django.db.models import Sum
from .choice import TRANSACTION_STATUS, TRANSACTION_TYPE_CHOICES, ACCOUNT_TYPE
from django.contrib import messages
# Create your views here.

#cashflow


class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())
        
class CashView(TemplateView):
    template_name= "cashflow.html"

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
    # def form_invalid(self, form):
    #     pprint(form.errors)
    #     return super().form_invalid(form)

    def get_context_data(self, **kwargs): 
        context = super(AddAccountView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context









##### TRANSACTIONS ########

class TransactionListView(RedirectPermissionRequiredMixin,  ListView): 
    template_name= "transaction_list.html"
    model = Transaction 
    permission_required = 'cashflow.view_cashflow'
    def get_context_data(self, **kwargs):
        context = super(TransactionListView, self).get_context_data(**kwargs)
        # context["transactions"] =Transaction.objects.all().order_by('date')
        filters=Transactionfilter(self.request.GET, queryset=Transaction.objects.all())
        # context["transactions"] = filters.qs
        context["transactions"] = Transaction.objects.all()
        context["transactions_count"] =Transaction.objects.all().count()
        context["total"] =Transaction.payments.get_total()
        
        context["transactions_paid"] = TransactionManager.get_total_paid_transactions(self)
        context["transactions_not_paid"] = TransactionManager.get_total_not_paid_transactions(self)
        context["transactions_pending"] = TransactionManager.get_total_pending_transactions(self)

        print("ssssssssdiiiiiifouuuuuuu#@#@#@##@#")

        # context["total_dettes"] = Project.objects.all().aggregate(Sum('get_project_dettes'))
        # context["total_payment"] =Transaction.payments.get_total_payment()
        # context["total_charges"] =Transaction.payments.get_total_charges()
        # context["total_creance"] =Transaction.payments.get_total_creance()
        # context["total_salaire"] =Transaction.payments.get_total_salaire()    
        # context["total_allouer"] =Transaction.payments.get_total_allouer()  

        def pie_chart(request):
            labels = []
            data = []
            # context["transactions"] = Transaction.objects.all()
            qs = Transaction.objects.order_by('-amount')[:5]
            print('QERYYY', qs)
            for tr in qs:
                print('TR', tr)
                labels.append(tr.name)
                data.append(int(tr.amount))
            print('labels',labels)
            print('data', data)

            return render(request, 'transaction_list.html', {
                'labels': labels,
                'data': data,
            })

        context["transactionstatus"] = TRANSACTION_STATUS
        return context

    def pie_chart(request):
        labels = []
        data = []
        # context["transactions"] = Transaction.objects.all()
        qs = Transaction.objects.order_by('-amount')[:5]
        print('QERYYY', qs)
        for tr in qs:
            print('TR', tr)
            labels.append(tr.name)
            data.append(int(tr.amount))
        print('labels',labels)
        print('data', data)

        return render(request, 'transaction_list.html', {
            'labels': labels,
            'data': data,
        })


   








class TransactionCreateView(RedirectPermissionRequiredMixin, CreateView):
    template_name= "transaction_create_model.html"
    model = Transaction 
    form_class= TransactionCreateForm
    permission_required = 'cashflow.create_cashflow'
    success_message = 'Transaction created seccussfully.'
    success_url = reverse_lazy('cashflow:transactionlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('cashflow:transactionlist')

    def get_context_data(self, **kwargs):
        context = super(TransactionCreateView, self).get_context_data(**kwargs)
        context["transactionstatus"] = TRANSACTION_STATUS
    #     context["companies"] = Company.objects.all()
    #     context["accounts"] = Account.objects.all()
    #     context["projects"] = Project.objects.all()
        return context

class TransactionUpdateView(RedirectPermissionRequiredMixin, UpdateView):
    template_name = "transaction_edit_model.html"
    model = Transaction
    form_class = TransactionCreateForm
    permission_required = 'cashflow.update_cashflow'
    success_url = reverse_lazy('cashflow:transactionlist')
    success_message = 'Transaction updated seccussfully.'
    
    def get_context_data(self, **kwargs):
        context = super(TransactionCreateView, self).get_context_data(**kwargs)
        context["transactionstatus"] = TRANSACTION_STATUS

        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('cashflow:transactionlist')


class TransactionDetailView(RedirectPermissionRequiredMixin, DetailView):
    template_name = "transaction_detail.html"
    model = Transaction
    form_class= AddAccountForm
    permission_required = 'cashflow.view_cashflow'
    success_url = reverse_lazy('cashflow:transactionlist')


class TransactionDeleteView(RedirectPermissionRequiredMixin, DeleteView):
    template_name = "transaction_delete_model.html"
    model = Transaction
    form_class = TransactionCreateForm
    permission_required = 'cashflow.delete_cashflow'
    success_url = reverse_lazy('cashflow:transactionlist')
    success_message = 'Transaction deleted seccussfully.'



















class ChartTestView(TemplateView):
    template_name = "dochart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = Transaction.objects.all()
        context["amounts"] = int(Transaction.objects.all())
        return context
        


def pie_chart(request):
    labels = []
    data = []
    # context["transactions"] = Transaction.objects.all()
    qs = Transaction.objects.order_by('-amount')[:5]
    print('QERYYY', qs)
    for tr in qs:
        print('TR', tr)
        labels.append(tr.name)
        data.append(int(tr.amount))
    print('labels',labels)
    print('data', data)

    return render(request, 'transaction_list.html', {
        'labels': labels,
        'data': data,
    })







