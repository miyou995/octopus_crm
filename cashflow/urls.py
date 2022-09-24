from django.urls import path

from .views import (
   CashView,
   CashflowAccountListView, 
   AccountDetailView, 
   AddAccountView, 
   CashflowListView,
   AddTransactionView,
)
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'cashflow'

urlpatterns = [  
   #cashflow
  
   path('accountlist', login_required(CashflowAccountListView.as_view()), name='accountlist'),
   path('accounttdetail/<int:pk>/', login_required(AccountDetailView.as_view()), name="accounttdetail"),
   path('addaccounts', login_required(AddAccountView.as_view()), name="addaccounts"),

   path('cashflow/transactionlist', login_required(CashflowListView.as_view()), name='cashflowlist'),
   path('cashflow/addtransaction', login_required(AddTransactionView.as_view()), name="addtransaction"),
   
]




