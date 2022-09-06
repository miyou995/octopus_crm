import django_filters 
from django_filters import DateFilter

from accounts.models import User
from .models import Company


class CompanyFilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
    )
    class Meta:
        model = Company
        fields = ['name', 'project_type', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)

class Userfilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
    ('EC', 'e-commerce'),
    ('WS', 'web site'),
    ('WA', 'web app'),
    )
    class Meta:
        model = User
        fields = ['name', 'project_type', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)