from django.urls import path
from cashflow import views
from .views import (
   CashView,
   AccountListView, 
   AccountDetailView, 
   AccountCreateView, 
   AccountUpdateView,
   TransactionListView,
   TransactionCreateView,
   TransactionUpdateView,
   TransactionDeleteView,
   TransactionDetailView,
   ChartTestView,

)
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'cashflow'

urlpatterns = [  
   #cashflow
  
   path('accountlist', login_required(AccountListView.as_view()), name='accountlist'),
   path('accountcreate', login_required(AccountCreateView.as_view()), name="accountcreate"),
   path('accountdetail/<int:pk>/', login_required(AccountDetailView.as_view()), name="accountdetail"),
   path('accountedit/<int:pk>/', login_required(AccountUpdateView.as_view()), name="accountedit"),

   path('cashflow/transactionlist', login_required(TransactionListView.as_view()), name='transactionlist'),
   path('cashflow/addtransaction', login_required(TransactionCreateView.as_view()), name="transactioncreate"),
   path('cashflow/transactionedit/<int:pk>', login_required(TransactionUpdateView.as_view()), name="transactionedit"),
   path('cashflow/transactiondelete/<int:pk>', login_required(TransactionDeleteView.as_view()), name="transactiondelete"),
   path('cashflow/transactiondetail/<int:pk>', login_required(TransactionDetailView.as_view()), name="transactiondetail"),
   path('chart/',login_required(ChartTestView.as_view()), name='chart'),
   # path('dochart/', views.pie_chart, name='dochart'),
]




