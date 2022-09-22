from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class InvoiceView(TemplateView):
    template_name = "invoice.html" 

class BillsView(TemplateView):
    template_name = "bills.html" 
