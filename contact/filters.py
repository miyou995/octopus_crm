import django_filters 
from django_filters import DateFilter

from accounts.models import User
from .models import Company


class CompanyFilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
        ('E-COMMERCE', 'e-commerce'),
        ('WEB SITE', 'web site'),
        ('WEB APP', 'web app'),
    )

    class Meta:
        model = Company
        fields = ['name', 'project_type', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)

class Userfilter(django_filters.FilterSet): 
    PROJECT_TYPE_CHOICES = (
        ('E-COMMERCE', 'e-commerce'),
        ('WEB SITE', 'web site'),
        ('WEB APP', 'web app'),
    )

    class Meta:
        model = User
        fields = ['name', 'collab_start']
    
    def filter_by_project_type(self, queryset, name, value): 
        expresssion = 'active' if value =='ascending' else '-active'
        return queryset.order_by(expresssion)