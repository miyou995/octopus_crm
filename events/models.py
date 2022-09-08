import email
from turtle import title
from unicodedata import name
from django.db import models
from contact.models import Company
from accounts.models import User
from project.choice import STATUS_TYPE_CHOICES
from project.models import Project

# Create your models here.

class event(models.Model):
    title           = models.CharField(max_length=180, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    start_date      = models.DateField()
    deadline        = models.DateField()
    start_time      = models.TimeField(blank=True, null=True)
    end_time        = models.TimeField(blank=True, null=True)

    company         = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='company_events')
    user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_events')

    def __str__(self):
        return self.title

    # @property
    #     def get_html_url(self):
    #         url = reverse('meetings:event_view', args=(self.id,))
    #         return f'<a href="{url}" style="text-decoration:none; color:#392C70;"> {self.title} </a>'


TICKET_STATUTE_TYPES = (
    ('OP', 'opened'),
    ('CL', 'closed'),
)


class Ticket(models.Model):
    title               = models.CharField(max_length=180)
    description         = models.TextField(blank=True, null=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    statute             = models.CharField(choices=TICKET_STATUTE_TYPES, max_length=2)

    projet              = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)

