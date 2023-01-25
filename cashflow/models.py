import imp
from secrets import choice
from django.db import models
from project.models import Project
from accounts.models import User
from django.db.models import Sum
from django.urls import reverse
from .choice import TRANSACTION_STATUS, TRANSACTION_TYPE_CHOICES, ACCOUNT_TYPE
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.shortcuts import render
from project.models import Project
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
    name                = models.CharField(max_length=252, db_index=True, blank=True, null=True)
    acc_type            = models.CharField(choices=ACCOUNT_TYPE, db_index=True, max_length=3,blank=True, null=True)
    actif               = models.BooleanField(blank=True, null=True)
    description         = models.TextField(blank=True, null=True)
    # postal_code         = models.PositiveIntegerField(default=0)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    project             = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE) # on_delete q4FQ#RF1234rf3

    objects             = models.Manager()
    account_managing    = AccountManager()

    def __str__(self):
        return self.name

    def get_account_edit_url(self):
        return reverse('cashflow:accountedit', kwargs={'pk':self.pk})

    def get_absolute_url(self):
        return reverse('cashflow:accountdetail', kwargs={'pk':self.pk})

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

    # def get_total_paid_transactions(self):
    #     p_t = Transaction.objects.filter(tr_status="PAID").aggregate(Sum('amount'))
    #     paid_transactions = float(p_t['amount__sum'])
    #     return paid_transactions

    def get_total_paid_transactions(self):
        return Transaction.objects.filter(tr_status="PAID").aggregate(Sum('amount'))

    def get_total_not_paid_transactions(self):
        return Transaction.objects.filter(tr_status="NOT_PAID").aggregate(Sum('amount'))

    def get_total_pending_transactions(self):
        return Transaction.objects.filter(tr_status="PENDING").aggregate(Sum('amount'))


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
    account_sd  = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender', blank=True, null=True) 
    account_rc  = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE, related_name='receiver') 
    tr_type     = models.CharField(choices=TRANSACTION_TYPE_CHOICES, max_length=2, null=True, blank=True)
    tr_status   = models.CharField(choices= TRANSACTION_STATUS, blank=True, null=True, max_length=13)
    other       = models.CharField(max_length=254, blank=True, null=True)
    amount      = models.DecimalField(max_digits=10 , decimal_places=2,validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    date        = models.DateField(blank=True, null=True)
    note        = models.CharField(max_length=254, blank=True, null=True)
    project     = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="transactions_project",blank=True, null=True,)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    objects     = models.Manager()
    payments    = TransactionManager()
    # amnt        = models.PositiveIntegerField()

    made_by     = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="made_transactions") 
    
    def __str__(self):
        # return f"{self.project} - {self.tr_type}"
        return self.name

    @property
    def get_absolute_url(self):
        return reverse("cashflow:transactiondetail", kwargs={"pk": self.pk})

    @property
    def get_edit_transaction_url(self):
        return reverse("cashflow:transactionedit", kwargs={"pk": self.pk})
    
    # @property
    # def get_total_paid_transactions(self):
    #     return Transaction.objects.filter(tr_status="PAID").aggregate(Sum('amount'))

