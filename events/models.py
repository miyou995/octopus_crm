import email
from pyexpat import model
from turtle import title
from unicodedata import name
from django.urls import reverse
from django.db import models
from contact.models import Company
from accounts.models import User
from project.choice import STATUS_TYPE_CHOICES
from project.models import Project
from .choice import EVENT_PRIORITY, TICKET_STATUTE_TYPES
from django.core.exceptions import ValidationError
from django.db.models import CheckConstraint, Q, F
from django.forms.utils import ErrorList
from django.utils.translation import gettext_lazy as _
import datetime
# from django.utils.timezone import datetime
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
        return str(self.name)

    @property
    def get_absolute_url(self):
        return reverse("events:eventdetail", kwargs={"pk": self.pk})

    # @property
    # def notification_time(self):
    #     return 

    # class Meta:
        # db_table = 'Event'
        # managed = True
        # constraints = [
        #     CheckConstraint(
        #         check=Q(deadline__gt=F('start_date')or Q(end_time__gt=F('start_time'))),
        #         name="date_check",
        #     ),
        # ]

    def clean(self):
        # Ensures constraint on model level, raises ValidationError
        if self.start_date > self.deadline :
            # raise error for field
            raise ValidationError(
                {
                    'deadline': _('End date cannot be smaller then start date.')
            }
            )
        if self.start_time > self.end_time:
               raise ValidationError(
                {
                    'end_time': _('End time cannot be smaller then start time')
            })

        if self.start_time < datetime.datetime.now().time() :
            raise ValidationError({
                'start_time': _('Start time connot be then todys time')
            })

        if self.start_date < datetime.date.today():
            raise ValidationError({
                'start_date': _('Start date connot be then todys date')
            })

        
            
    # def clean(self):
    #     # deadline = self.cleaned_data.get('deadline')
    #     # end_time = self.cleaned_data.get('end_time')
    #     if self.start_date > self.deadline:
    #         if not self._errors.has_key('deadline'):
    #             # self._errors['deadline'] = ErrorList()
    #             self._errors['deadline'].append('End date cannot be smaller then start date.')
    #     if self.start_time > self.end_time:
    #         # if not self._errors.has_key('end_time'):
                
    #         self._errors['end_time'] = ErrorList()
    #         self._errors['end_time'].append('End time cannot be smaller then start time')
            # try:
            #     bus_route.save()
            # except IntegrityError as err:
            #     raise CustomException('CUSTOM ERROR MESSAGE')

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