import django_filters 
from django_filters import DateFilter
from .models import Account
from .models import Transaction


class Accountfilter(django_filters.FilterSet): 
    class Meta:
        model = Account
        fields = ['name', 'acc_type', 'created']
    
    def filter_by_type(self, queryset, name, value): 
        expresssion = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expresssion)
    def filter_by_owner(self, queryset, name, value): 
        expresssion = 'created' if value =='ascending' else '-created'
        return queryset.order_by(expresssion)




class Transactionfilter(django_filters.FilterSet): 
    class Meta:
        model = Transaction  #tW#$T@$Rf2r4@#R2#f234f2
        fields = [ 'tr_type', 'date']

    def filter_by_type(self, queryset, name, value): 
        expresssion = 'date' if value =='ascending' else '-date'
        return queryset.order_by(expresssion)
    def filter_by_account(self, queryset, name, value): 
        expresssion = 'date' if value =='ascending' else '-date'
        return queryset.order_by(expresssion)
