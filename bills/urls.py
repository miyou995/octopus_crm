from django.urls import path

from bills.views import BillsView, InvoiceView

app_name = 'bills'

urlpatterns = [
    
  path('invoice/',InvoiceView.as_view(), name='invoice'),
  path('bills/',BillsView.as_view(), name='bills'),
]