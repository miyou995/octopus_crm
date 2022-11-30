from msilib.schema import Class
from pyexpat import model
from django.forms import ModelForm
from .models import Invoice, Proforma, BillItem, Bill

from django.forms.models import inlineformset_factory

class InvoiceCreateForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class ProformaCreateForm(ModelForm):
    class Meta:
        model = Proforma
        fields = '__all__'

class BillItemCreateForm(ModelForm):
    class Meta:
        model = BillItem
        fields = '__all__'

BillItemFormset = inlineformset_factory(Bill, BillItem,
 fields=('name', 'quantity', 'price'),
 extra=1)