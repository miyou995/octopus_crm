from django import forms
from .models import Contact, Invoice

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','email','subject','message']
 

def must_be_empty(value):
    if value:
        raise forms.ValidationError('ce champs doit etre vide')

class ContactForm(forms.Form):
    name = forms.CharField(required = True, max_length=150) 
    email = forms.CharField(max_length=254)
    phone = forms.CharField(max_length=25)
    subject = forms.CharField(max_length=300) 
    honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])
    message = forms.CharField()    

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('client', 'client_rc', 'client_nif', 'client_art', 'client_adresse', 'invoice_number', 'invioce_date', 'note', 'discount',)
        required = ('client',)
       
