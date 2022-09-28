from django.urls import path
from django.contrib.auth.decorators import login_required

from bills.views import InvoiceCreateView, InvoiceDeleteView, InvoiceDetailView, InvoiceListView, InvoiceUpdateView
from .views import ProformaCreateView, ProformaDeleteView, ProformaDetailView, ProformaUpdateView, ProformaListView

app_name = 'bills'

urlpatterns = [
    
  path('invoice/create',login_required(InvoiceCreateView.as_view()), name='invoicecreate'),
  path('invoice/update/<int:pk>',login_required(InvoiceUpdateView.as_view()), name='invoiceedit'),
  path('invoice/delete/<int:pk>',login_required(InvoiceDeleteView.as_view()), name='invoicedelete'),
  path('invoice/detail/<int:pk>',login_required(InvoiceDetailView.as_view()), name='invoicedetail'),
  path('invoice/',login_required(InvoiceListView.as_view()), name='invoicelist'),

# Proforma urls 
  path('proforma/create',login_required(ProformaCreateView.as_view()), name='proformacreate'),
  path('proforma/update/<int:pk>',login_required(ProformaUpdateView.as_view()), name='proformaedit'),
  path('proforma/delete/<int:pk>',login_required(ProformaDeleteView.as_view()), name='proformadelete'),
  path('proforma/detail/<int:pk>',login_required(ProformaDetailView.as_view()), name='proformadetail'),
  path('proforma/',login_required(ProformaListView.as_view()), name='proformalist'),
]