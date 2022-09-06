from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from tinymce import models as tinymce_models
from .choice import *
from contact.models import Company


class UserManager(BaseUserManager):
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
    role            = models.CharField( max_length=150, null=True, blank=True)
    decision        = models.CharField(choices=DECISION_TYPE_CHOICES, max_length=2, blank=True, null=True)
    mobile          = models.CharField(max_length=13, blank=True, null=True)


    notes           = tinymce_models.HTMLField( blank=True, null=True)
    is_active       = models.BooleanField(default=False)
    is_manager      = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []
    user_type       = models.CharField(choices=USER_TYPE_CHOICES, max_length=2, blank=True, null=True)
    fonction        = models.CharField(choices=FUNCTION_TYPE_CHOICE, max_length=2, blank=True, null=True)
    client_lead     = models.CharField(choices=LEADSTATUTE_TYPE_CHOICE, max_length=256)
    project_type    = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=2, blank=True, null=True)
    collab_start    = models.DateField(blank=True, null=True)
    source          = models.CharField( max_length=250, blank=True, null=True)
    
    created         = models.DateField(auto_now=True)
    updated         = models.DateField(auto_now_add=True)
    company         = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='reel_users')
    objects         = UserManager()


    def __str__(self):
        return str(self.company)


