from xml.parsers.expat import model
from django.forms import ModelForm
from .models import Company
from accounts.models import User


class CompanyAddForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__' 
    
    # def form_valid(self, form):
    #     return super().form_valid(form)


class AddClientForm(ModelForm):
    class Meta:
        model = User
        fields =['name', 'company', 'mobile', 'role', 'decision', 'email', 'collab_start', 'source', 'password', 'is_responsible', 'is_internal' ]