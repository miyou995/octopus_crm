from django import forms
from django.forms import ModelForm, widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import  Account, Transaction

class AddAccountForm(ModelForm) :
    class Meta: 
        model = Account
        fields = '__all__' 
    
class AddTransactionForm(ModelForm) :
    class Meta: 
        model = Transaction
        fields = '__all__' 
