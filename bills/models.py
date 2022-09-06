from django.db import models
from project.models import Project
from cashflow.models import Account, Transaction


# Create your models here.

class BillItem(models.Model):
    name            = models.CharField(max_length=180, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    quantity        = models.IntegerField(blank=True, null=True)
    tax             = models.BooleanField(default=False)
    tva             = models.BooleanField(default=False)
    note            = models.TextField(blank=True, null=True)
    term            = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True

class Bill(BillItem, models.Model):
    # logo              = models.ImageField()
    number              = models.IntegerField(blank=True, null=True)
    phone               = models.CharField(max_length=13, blank=True, null=True)
    price               = models.DecimalField(max_digits=100000, decimal_places=0)
    discount            = models.DecimalField(max_digits=100000, decimal_places=0)
    # description         = models.TextField(blank=True, null=True)
    # city                = city.Field()
    # address             = city.Field()
    postal_code         = models.DecimalField(max_digits=7,decimal_places=0, blank=True, null=True)
    to_name             = models.CharField(max_length=180, blank=True, null=True)
    # to_address          = city.Field()
    # to_city             = city.Field()
    to_postal_code      = models.DecimalField(max_digits=7,decimal_places=0, blank=True, null=True)
    to_phone            = models.CharField(max_length=13, blank=True, null=True)


    created             = models.DateTimeField(auto_now=True)
    updated             = models.DateTimeField(auto_now_add=True)

    # account             = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='account_bills')
    class Meta(BillItem.Meta):
        abstract = True











class Invoice(Bill, models.Model):
    account     = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL) #on_delete $@!FWFEF@#$F

    def __str__(self):
        return self.number

        

class Proforma(Bill, models.Model):
    account     = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL) #on_delete $@!FWFEF@#$F

    def __str__(self):
        return self.number
