from ast import Return
# from multiprocessing import Event
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView, 
    FormView
)
from events.models import Event
from project.models import Project
from contact.models import Company
from django.contrib import messages
from django.http import response
# Create your views here.
#Dashboard 


class IndexView(TemplateView):
    template_name= "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["projects"] = Project.objects.all().order_by('started_date')
        context["subscriptions"] = Project.objects.all().order_by('contract_expiration')
        context["project_count"] =Project.objects.all().count()
        context["companies"] = Company.objects.all().order_by('collab_start')
        context["company_count"] =Company.objects.all().count()
        # context["events"] = Event.objects.all()
        # context["employees"] = Employee.objects.all().order_by('collab_start')
        # context["client_count"] =Employee.objects.all().count()
        # context["leads"] = Lead.objects.all().order_by('updated')
        # context["lead_count"] =Lead.objects.all().count()
        return context 



class TestView(TemplateView):
    template_name = "test.html" 



