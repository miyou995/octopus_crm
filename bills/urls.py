from django.urls import path

from bills.views import InvoiceView

app_name = 'bills'

urlpatterns = [
    
  path('invoice',InvoiceView.as_view(), name='invoice'),
    
]