from django.db import models
from .choice import *
from django.urls import reverse
# from accounts.models import User

class CompanyQueryset(models.QuerySet):
    def is_client(self):
        return Company.objects.filter(company_type='CL')

    def is_fournisseur(self):
        return Company.objects.filter(company_type='F')
    
    def is_partenaire(self):
        return Company.objects.filter(company_type='P')
    
    def is_concurrent(self):
        return Company.objects.filter(company_type='CN')



class CompanyManager(models.Manager):
    queryset        = CompanyQueryset()
    def is_client(self):
        return Company.objects.filter(company_type='CL')

    def is_fournisseur(self):
        return Company.objects.filter(company_type='F')
    
    def is_partenaire(self):
        return Company.objects.filter(company_type='P')
    
    def is_concurrent(self):
        return Company.objects.filter(company_type='CN')


class Company(models.Model):
    name                = models.CharField(max_length=250)
    industry            = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue      = models.DecimalField(max_digits=20 , decimal_places=0, blank=True, null=True)
    email               = models.EmailField(max_length=254,  blank=True, null=True)
    mobile              = models.CharField(max_length=13,  blank=True, null=True)
    website             = models.URLField(max_length=250, blank=True, null=True)
    adress              = models.CharField(max_length=250,  blank=True, null=True)
    rc_code             = models.CharField( max_length=150, null=True, blank=True)
    art_code            = models.CharField(max_length=150, null=True, blank=True)
    nif_code            = models.CharField( max_length=150, null=True, blank=True)
    nis_code            = models.CharField( max_length=150, null=True, blank=True)
    source              = models.CharField(max_length=250, blank=True, null=True)
    company_type        = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=2, blank=True, null=True)
    project_type        = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    logo                = models.ImageField(upload_to='companies/', null=True, blank=True)  
    collab_start        = models.DateField(blank=True, null=True)
    created             = models.DateField(auto_now=True)
    updated             = models.DateField(auto_now_add=True)
    postal_code         = models.IntegerField(blank=True, null=True)
    responsible_person  = models.CharField(max_length=100,  blank=True, null=True)


    objects             = CompanyManager()
    # camopany_managing   = CompanyQueryset().as_manager()

    def __str__(self):
        return self.name
        
    @property
    def get_absolute_url(self):
        return reverse("contact:companydetail", kwargs={"pk": self.pk})

    @property
    def is_responsible_person(self):
        return self.responsible_person


