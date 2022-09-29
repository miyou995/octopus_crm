from tokenize import Triple
from unicodedata import name
from django.db import models
from contact.models import Company
from accounts.models import User
from tinymce import models as tinymce_models
from .choice import *
from django.db.models import Sum
from django.urls import reverse
from .choice import CONTRACT_TYPE_CHOICES
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class ProjectQueryset(models.QuerySet):
    def is_ecommerce(self):
        return Project.objects.filter(project_type='EC')
    
    def is_website(self):
        return Project.objects.filter(project_type='WS')
    
    def is_webapp(self):
        return Project.objects.filter(project_type='WA')
    
    # CONTRACT TYPE
    def is_hosting(self):
        return Project.objects.filter(contract='H')
    
    def is_annual(self):
        return Project.objects.filter(contract='A')
    
    def is_semi_annual(self):
        return Project.objects.filter(contract='S')
    
    def is_quarterly(self):
        return Project.objects.filter(contract='Q')
    
    def is_advertisement(self):
        return Project.objects.filter(contract='AD')


# STATUS TYPES
    def is_confirmed(self):
        return Project.objects.filter(status='CF')
    
    def is_completed(self):
        return Project.objects.filter(status='CP')
    def is_pending(self):
        return Project.objects.filter(status='PE')

    def is_cancelled(self):
        return Project.objects.filter(status='CA')

class ProjectManager(models.Manager):
    queries = ProjectQueryset()

    def is_ecommerce(self):
        return Project.objects.filter(project_type='EC')
    
    def is_website(self):
        return Project.objects.filter(project_type='WS')
    
    def is_webapp(self):
        return Project.objects.filter(project_type='WA')
    
    # CONTRACT TYPE
    def is_hosting(self):
        return Project.objects.filter(contract='H')
    
    def is_annual(self):
        return Project.objects.filter(contract='A')
    
    def is_semi_annual(self):
        return Project.objects.filter(contract='S')
    
    def is_quarterly(self):
        return Project.objects.filter(contract='Q')
    
    def is_advertisement(self):
        return Project.objects.filter(contract='AD')


# STATUS TYPES
    def is_confirmed(self):
        return Project.objects.filter(status='CF')
    
    def is_completed(self):
        return Project.objects.filter(status='CP')
    def is_pending(self):
        return Project.objects.filter(status='PE')

    def is_cancelled(self):
        return Project.objects.filter(status='CA')



# Create your models here.
class Project (models.Model): 
    name                    = models.CharField(max_length=254, blank=True, null=True)
    cost                    = models.DecimalField(max_digits=20 , decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    started_date            = models.DateField(blank=True, null=True) 
    deadline                = models.DateField(blank=True, null=True) 
    project_type            = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract                = models.CharField(choices=CONTRACT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    contract_expiration     = models.DateField(blank=True, null=True) 
    status                  = models.CharField(choices=STATUS_TYPE_CHOICES, max_length=2, blank=True, null=True)
    description             = tinymce_models.HTMLField( blank=True, null=True)
    created                 = models.DateTimeField(auto_now_add=True)
    updated                 = models.DateTimeField(auto_now=True)

    company                 = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True,  verbose_name="client", related_name="projects") 
    manager                 = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="manager", related_name='project_managers') 
    team                    = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,verbose_name="team", related_name='project_teams')

    objects                 = models.Manager()
    managing                = ProjectManager()


    def __str__(self):
        return self.name
    
    @property
    def get_absolute_url(self):
        return reverse("project:projectdetail", kwargs={"pk": self.pk})
    

    def clean(self):
        # Ensures constraint on model level, raises ValidationError
        if self.started_date > self.deadline :
            # raise error for field
            raise ValidationError(
                {
                    'deadline': _('End date cannot be smaller then start date.')
            }
            )


        
    # @property
    # def get_status_class(self):
    #     if self.status == "CF":
    #         return "badge-success"
    #     elif self.status == "CP":
    #         return "badge-info"
    #     elif self.status == "PE":
    #         return "badge-warning"
    #     else:
    #         return "badge-danger"
    
    # def get_project_dettes(self):
    #     cost = self.cost
    #     transactions = self.transactions.aggregate(Sum('amount'))
    #     reste = self.cost - transactions['amount__sum']
    #     return int(reste)



class Task(models.Model):
    name                = models.CharField(max_length=256, blank=True, null=True)
    started_date        = models.DateField(blank=True, null=True) 
    deadline            = models.DateField(blank=True, null=True)
    created             = models.DateTimeField(auto_now_add=True)
    description         = tinymce_models.HTMLField( blank=True, null=True)
    updated             = models.DateTimeField(auto_now=True)

    project             = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='tasks')
    user                = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='supervised_tasks')

    def __str__(self):
        return self.name


   