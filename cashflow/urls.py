from django.urls import path

from .views import (
   CashView,
   CashflowAccountListView, 
   AccountDetailView, 
   AddAccountView, 
   TransactionListView,
   TransactionCreateView,
)
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'cashflow'

urlpatterns = [  
   #cashflow
  
   path('accountlist', login_required(CashflowAccountListView.as_view()), name='accountlist'),
   path('accounttdetail/<int:pk>/', login_required(AccountDetailView.as_view()), name="accounttdetail"),
   path('addaccounts', login_required(AddAccountView.as_view()), name="addaccounts"),

   path('cashflow/transactionlist', login_required(TransactionListView.as_view()), name='transactionlist'),
   path('cashflow/addtransaction', login_required(TransactionCreateView.as_view()), name="transactioncreate"),
   
]




