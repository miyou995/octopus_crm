from django.urls import path
from .views import CompanyListView, CompanyAddView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView
from .views import  ClientListView, AddClientView, ClientUpdateView, ClientDetailView, ClientDeleteView,InternalEmployeeListView, AddInternalEmployeeView

from django.contrib.auth.decorators import login_required

app_name = 'contact'

urlpatterns = [
    path('companylist/', login_required(CompanyListView.as_view()), name='companylist'),
    path('companylist/create/',login_required(CompanyAddView.as_view()), name='addcompany'),
    path('editcompany/<int:pk>/',login_required(CompanyUpdateView.as_view()), name='editcompany'),
    path('deletecompany/<int:pk>/',login_required(CompanyDeleteView.as_view()), name='companydelete'),
    path('detailcompany/<int:pk>/',login_required(CompanyDetailView.as_view()), name='companydetail'),
    #CLIENT
    path('clientlist', login_required(ClientListView.as_view()), name='clientlist'),
    path('clientlist/addclient', login_required(AddClientView.as_view()), name="addclient"),
    path('editclient/<int:pk>/', login_required(ClientUpdateView.as_view()), name="editclient"),
    path('clientdetail/<int:pk>/', login_required(ClientDetailView.as_view()), name="clientdetail"),
    path('clientdelete/<int:pk>/', login_required(ClientDeleteView.as_view()), name="clientdelete"),
    path('internalemployeelist', login_required(InternalEmployeeListView.as_view()), name='internalemployeelist'),
    path('internalemployeelist/addinternalemployee', login_required(AddInternalEmployeeView.as_view()), name='addinternalemployee'),
    


]

