from ast import Delete
from msilib.schema import ListView
from multiprocessing import context
import re
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
# from django.views.generic import (
#     DetailView,
#     UpdateView,
#     ListView,
#     DeleteView, 
#     FormView
# )
from .forms import InvoiceCreateForm, ProformaCreateForm, BillItemCreateForm
from django.urls.base import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


from django.http import HttpResponse
from django.views.generic import View
# from .process import html_to_pdf 

from .models import Bill, BillItem, Invoice, Proforma




class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())


class InvoiceListView(RedirectPermissionRequiredMixin, ListView):
    model = Invoice
    template_name = 'invoice_list.html'
    permission_required = 'invoice.view_invoice'

    def get_context_data(self, **kwargs):
        context = super(InvoiceListView, self).get_context_data(**kwargs)
        context["invoices"] = Invoice.objects.all()
        return context


class InvoiceCreateView(RedirectPermissionRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = "invoice_create_model.html"
    permission_required = 'invoice.create_invoice'
    seccess_message = 'Invoice created seccessfully.'

    success_url = reverse_lazy('bills:invoicelist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('bills:invoicelist')
    
class InvoiceUpdateView(RedirectPermissionRequiredMixin, UpdateView):
    model = Invoice
    template_name = 'invoice_update_model.html'
    permission_required = 'invoice.update_invoice'
    success_url = reverse_lazy("bills:invoicelist")
    success_message = 'Invoice Updated Seccessfully'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('bills:invoicelist')

class InvoiceDetailView(RedirectPermissionRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'invoice_detail.html'
    permission_required = 'invoice.detail_invoice'
    success_url = reverse_lazy("bills:invoicedetail")

class InvoiceDeleteView(RedirectPermissionRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'invoice_delete_model.html'
    permission_required = 'invoice.delete_invoice'
    success_url = reverse_lazy("bills:invoicelist")
    success_message = 'Invoice Deleted Seccessfully'


    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('bills:invoicelist')

# ##### PROFORMA

class ProformaListView(RedirectPermissionRequiredMixin, ListView):
    model = Proforma
    template_name = 'proforma_list.html'
    permission_required = 'proforma.view_proforma'

    def get_context_data(self, **kwargs):
        context = super(ProformaListView, self).get_context_data(**kwargs)
        context["proformas"] = Proforma.objects.all()
        return context


class ProformaCreateView(RedirectPermissionRequiredMixin, CreateView):
    model = Proforma
    form_class = ProformaCreateForm
    template_name = "proforma.html" 
    permission_required = 'proforma.create_proforma'
    seccess_message = 'Proforma created seccessfully.'
    success_url = reverse_lazy('bills:proformalist')


    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('bills:proformalist')

class ProformaUpdateView(RedirectPermissionRequiredMixin, UpdateView):
    model = Proforma
    template_name = 'proforma_update_model.html'
    permission_required = 'proforma.update_proforma'
    success_url = reverse_lazy("bills:proformalist")
    success_message = 'Proforma Updated Seccessfully'

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error comited please enter your real informtions")
        return redirect('bills:proformalist')

class ProformaDetailView(RedirectPermissionRequiredMixin, DeleteView):
    model = Proforma
    template_name = 'proforma_detail.html'
    permission_required = 'proforma.detail_proforma'
    success_url = reverse_lazy("bills:proformadetail")

class ProformaDeleteView(RedirectPermissionRequiredMixin, DeleteView):
    model = Proforma
    template_name = 'proforma_delete_model.html'
    permission_required = 'proforma.delete_proforma'
    success_url = reverse_lazy("bills:proformalist")
    success_message = 'Proforma Deleted Seccessfully'
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('bills:proformalist')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):    
        # getting the template
        # pdf = html_to_pdf('invoice_create_model.html')    
        #  # rendering the template
        # return HttpResponse(pdf, content_type='application/pdf')
        pass


class BillItemCreateView(CreateView):
    model = BillItem
    form_class = BillItemCreateForm

class BillItemDeleteView(DeleteView):
    model = BillItem
    # form_class = BillItemCreateForm
