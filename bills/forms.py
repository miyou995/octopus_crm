from msilib.schema import Class
from pyexpat import model
from django.forms import ModelForm
from .models import Invoice, Proforma, BillItem

class InvoiceCreateForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class ProformaCreateForm(ModelForm):
    class Meta:
        model = Proforma
        fields = '__all__'
