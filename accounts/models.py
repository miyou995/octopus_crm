# import imp
from email.policy import default
from sys import flags
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from tinymce import models as tinymce_models
from .choice import *
from contact.models import Company
from django.urls import reverse



class UserQueryset(models.QuerySet):
   
    # MY QS @@@@@@@@@@@@@@@@2
    def is_employee(self):
        return self.is_active and (self.is_superuser or self.is_staff and User.objects.filter(user_type='EM'))

    def is_employee(self):
        return self.is_active and (self.is_superuser or self.is_staff and User.objects.filter(user_type='CL')) 

# ROLE TYPES
    def is_assistant(self):
        return self.objects.filter(role='AS')

    def is_developer(self):
        return self.objects.filter(role='DV')

    def is_commercial(self):
        return self.objects.filter(role='CM')

    def is_marketer(self):
        return self.objects.filter(role='MK')

    def is_content_creator(self):
        return self.objects.filter(role='CC')

    def is_designer(self):
        return self.objects.filter(role='DS')

#  CLIENT LEAD

    def get_client_interested(self):
        return self.objects.filter(client_lead='I')

    def get_client_call_again(self):
        return self.objects.filter(client_lead='CA')

    def get_client_not_interested(self):
        return self.objects.filter(client_lead='NI')

    def is_internal_emp(self):
        return User.objects.filter(is_internal= True)

    @property
    def is_internal_empl(self):
        return User.objects.filter(is_internal= True)

class UserManager(BaseUserManager):
    user_queryset     = UserQueryset()
    use_in_migrations = True

    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)
       
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_internal", True)
        if extra_fields.get("is_staff") is not True:
         raise ValueError(
                "Superuser must have is_staff=True."
        )
        if extra_fields.get("is_active") is not True:
         raise ValueError(
                "Superuser must have is_active=True."
        )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                 "Superuser must have is_superuser=True."
        )
        return self._create_user(email, password, **extra_fields)
    




class User(AbstractUser):
    username        = None
    name            = models.CharField(max_length=120, blank=True, null=True)
    email           = models.EmailField('email address', unique=True)

    picture         = models.ImageField(upload_to='images/faces', null=True, blank=True)
    pseudo          = models.CharField( max_length=150, null=True, blank=True)
    role            = models.CharField(choices=ROLE_TYPE_CHOICE, max_length=20, blank=True, null=True)
    decision        = models.CharField(choices=DECISION_TYPE_CHOICES, max_length=2, blank=True, null=True)
    mobile          = models.CharField(max_length=13, unique=True, blank=True, null=True)


    notes           = tinymce_models.HTMLField( blank=True, null=True)
    is_active       = models.BooleanField(default=False)
    is_manager      = models.BooleanField(default=False)
    is_responsible  = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_internal     = models.BooleanField(default=False)
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    user_type       = models.CharField(choices=USER_TYPE_CHOICES, max_length=20, blank=True, null=True)
    client_lead     = models.CharField(choices=LEADSTATUTE_TYPE_CHOICE, max_length=20, blank=True, null=True)
    project_type    = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=20, blank=True, null=True)
    project_name    = models.CharField(max_length=120, blank=True, null=True)
    collab_start    = models.DateField(blank=True, null=True)
    source          = models.CharField( max_length=250, blank=True, null=True)
    
    created         = models.DateField(auto_now=True)
    updated         = models.DateField(auto_now_add=True)
    company         = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='users_company')
    objects         = UserManager()


    def __str__(self):
        return self.email
    
    @property
    def get_absolute_url(self):
        return reverse("contact:clientdetail", kwargs={'pk': self.pk})
    
    @property
    def is_assistant(self):
        return self.is_active and (self.is_superuser or self.is_staff and self.groups.filter(name="Assistant").exists())
    @property
    def is_developer(self):
        return self.is_active and (self.is_superuser or self.is_staff and self.groups.filter(name="Developer").exists())
    @property
    def is_commercial(self):
        return self.is_active and (self.is_superuser or self.is_staff and self.groups.filter(name="Commercial").exists())
    @property
    def is_marketer(self):
        return self.is_active and (self.is_superuser or self.is_staff and self.groups.filter(name="Marketer").exists() )
    @property
    def is_content_creator(self):
        return self.is_active and (self.is_superuser or self.is_staff and self.groups.filter(name="Content_creator").exists())

    # @property
    # def is_internal_emp(self):
    #     return self.is_internal