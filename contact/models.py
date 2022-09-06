from django.db import models
from .choice import *




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
    responsible_person  = models.CharField(max_length=100,  blank=True, null=True)
    source              = models.CharField(max_length=250, blank=True, null=True)
    company_type        = models.CharField(choices=COMPANY_TYPE_CHOICES, max_length=2, blank=True, null=True)
    project_type        = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    logo                = models.ImageField(upload_to='companies/', null=True, blank=True)  
    collab_start        = models.DateField(blank=True, null=True)
    created             = models.DateField(auto_now=True)
    updated             = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("contact:companydetail", kwargs={"pk": self.pk})




