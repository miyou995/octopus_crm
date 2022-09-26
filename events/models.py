import email
from pyexpat import model
from turtle import title
from unicodedata import name
from django.db import models
from contact.models import Company
from accounts.models import User
from project.choice import STATUS_TYPE_CHOICES
from project.models import Project
from .choice import EVENT_PRIORITY, TICKET_STATUTE_TYPES

# Create your models here.


class Event(models.Model):
    name            = models.CharField(max_length=180, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    start_date      = models.DateField(blank=True, null=True)
    deadline        = models.DateField(blank=True, null=True)
    start_time      = models.TimeField(blank=True, null=True)
    end_time        = models.TimeField(blank=True, null=True)
    priority        = models.CharField(choices=EVENT_PRIORITY, max_length=8, blank=True, null=True)
    company         = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='company_events')
    user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_events')

    def __str__(self):
        return self.name

    # @property
    #     def get_html_url(self):
    #         url = reverse('meetings:event_view', args=(self.id,))
    #         return f'<a href="{url}" style="text-decoration:none; color:#392C70;"> {self.title} </a>'





class Ticket(models.Model):
    name                = models.CharField(max_length=180, blank=True, null=True)
    description         = models.TextField(blank=True, null=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    status              = models.CharField(choices=TICKET_STATUTE_TYPES, max_length=2, blank=True, null=True)

    projet              = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name