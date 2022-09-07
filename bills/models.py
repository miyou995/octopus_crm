from django.db import models
from project.models import Project
from cashflow.models import Account, Transaction



class Bill(models.Model):
    # logo              = models.ImageField()
    cost        = models.DecimalField(max_digits=100000, decimal_places=0)
    discount    = models.DecimalField(max_digits=100000, decimal_places=0)
    from_company= models.ForeignKey("contact.Company",related_name="bills_sent", on_delete=models.CASCADE)
    to_companty = models.ForeignKey("contact.Company",related_name="bills_received", on_delete=models.CASCADE)
    account     = models.ForeignKey("cashflow.Account", related_name="invoice_account", on_delete=models.CASCADE) #on_delete $@!FWFEF@#$F

    created             = models.DateTimeField(auto_now=True)
    updated             = models.DateTimeField(auto_now_add=True)
    # description         = models.TextField(blank=True, null=True)
    # city                = city.Field()
    # address             = city.Field()
    # to_name             = models.CharField(max_length=180, blank=True, null=True)
    # # to_address          = city.Field()
    # # to_city             = city.Field()
    # to_postal_code      = models.DecimalField(max_digits=7,decimal_places=0, blank=True, null=True)
    # to_phone            = models.CharField(max_length=13, blank=True, null=True)
    # account             = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='account_bills')

    # class Meta:
    #     abstract = True
        


class Invoice(Bill):
    # invoice_bill = models.OneToOneField(Bill, on_delete=models.CASCADE, parent_link=True)
    number = models.IntegerField(default = 0 , verbose_name="Numéro de facture")
    class Meta:
        default_related_name = 'Invoice'

class Proforma(Bill):
    # proforma_bill = models.OneToOneField(Bill, on_delete=models.CASCADE, parent_link=True)
    number  = models.IntegerField(default = 0 , verbose_name="Numéro de Proforma")
    class Meta:
        default_related_name = 'Proforma'


class BillItem(models.Model):
    name        = models.CharField(max_length=180, blank=True, null=True)
    bill_ofc    = models.ForeignKey(Bill, related_name="items", on_delete=models.CASCADE) #on_delete $@!FWFEF@#$F
    description = models.TextField(blank=True, null=True)
    quantity    = models.IntegerField(blank=True, null=True)
    tax         = models.BooleanField(default=False)
    tva         = models.BooleanField(default=False)
    note        = models.TextField(blank=True, null=True)
    term        = models.TextField(blank=True, null=True)
    



