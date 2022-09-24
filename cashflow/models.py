from secrets import choice
from django.db import models
from project.models import Project
from accounts.models import User
from django.db.models import Sum
from .choice import TRANSACTION_STATUS, TRANSACTION_TYPE_CHOICES, ACCOUNT_TYPE

# Create your models here.



class AccountQueryset(models.QuerySet):
    def get_actif_account(self):
        return Account.objects.filter(actif=True)

    def get_inactif_account(self):
        return Account.objects.filter(actif=False)
    
    def get_account_in(self):
        return Account.objects.filter(acc_type='IN')
    
    def get_account_out(self):
        return Account.objects.filter(acc_type='OUT')

class AccountManager(models.Manager):
    queries = AccountQueryset
    def get_actif_account(self):
        return Account.objects.filter(actif=True)

    def get_inactif_account(self):
        return Account.objects.filter(actif=False)
    
    def get_account_in(self):
        return Account.objects.filter(acc_type='IN')
    
    def get_account_out(self):
        return Account.objects.filter(acc_type='OUT')



class Account(models.Model): 
    # owner        = models.ManyToManyField(Project, related_name="project_name" )
    name                = models.CharField(max_length=250, db_index=True)
    acc_type            = models.CharField(choices=ACCOUNT_TYPE, db_index=True, max_length=2,blank=True, null=True)
    actif               = models.BooleanField()
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    project             = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL) # on_delete q4FQ#RF1234rf3

    objects             = models.Manager()
    account_managing    = AccountManager()

    def __str__(self):
        return str(self.name)


class TransactionManager(models.Manager):
    def get_total(self):
        return Transaction.objects.all().aggregate(Sum('amount'))
    def get_total_payment(self):
        return Transaction.objects.filter(tr_type="PA").aggregate(Sum('amount'))
    def get_total_salaire(self):
        return Transaction.objects.filter(tr_type="SA").aggregate(Sum('amount'))
    def get_total_creance(self):
        return Transaction.objects.filter(tr_type="CR").aggregate(Sum('amount'))
    def get_total_charges(self):
        return Transaction.objects.filter(tr_type="CH").aggregate(Sum('amount'))
    def get_total_allouer(self):
        return Transaction.objects.filter(tr_type="AL").aggregate(Sum('amount'))
    def get_account_payment(self, account_id):
        return Transaction.objects.filter(tr_type="PA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_salaire(self, account_id):
        return Transaction.objects.filter(tr_type="SA", account_id = account_id).aggregate(Sum('amount'))
    def get_account_creance(self, account_id):
        return Transaction.objects.filter(tr_type="CR", account_id = account_id).aggregate(Sum('amount'))
    def get_account_charges(self, account_id):
        return Transaction.objects.filter(tr_type="CH", account_id = account_id).aggregate(Sum('amount'))
    def get_account_allouer(self, account_id):
        return Transaction.objects.filter(tr_type="AL", account_id = account_id).aggregate(Sum('amount'))



class Transaction(models.Model): 

    name        = models.CharField(max_length=180, blank=True, null=True)
    account_sd  = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='sender') 
    account_rc  = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='receiver') 
    tr_type     = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length=2, null=True, blank=True)
    tr_status   = models.CharField(choices= TRANSACTION_STATUS, blank=True, null=True, max_length=13)
    other       = models.CharField(max_length=254, blank=True, null=True)
    amount      = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    date        = models.DateField(blank=True, null=True)
    note        = models.CharField(max_length=254, blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    objects     = models.Manager()
    payments    = TransactionManager()

    made_by     = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="made_transactions") 
    
    def __str__(self):
        return f"{self.project} - {self.tr_type}"

