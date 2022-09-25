from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    FormView
)
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from events.forms import AddEventForm

from .models import Event

class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())

class CalendarView(TemplateView):
    template_name = "calendar.html" 


class EventsListView(RedirectPermissionRequiredMixin, ListView):
    template_name = "events_list.html" 
    model = Event
    # form_class = AddEventForm
    permission_required = 'events.view_event'

class EventCreateView(RedirectPermissionRequiredMixin, CreateView):
    template_name = 'event_create_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.create_event'
    success_message = "Event created successfully."
    success_url = reverse_lazy('events:eventcreate')


class EventUpdateView(RedirectPermissionRequiredMixin, UpdateView):
    template_name = 'event_edit_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.create_event'
    success_message = "Event updated successfully."
    success_url = reverse_lazy('events:eventcreate')


class EventDetailView(RedirectPermissionRequiredMixin, DetailView):
    template_name = 'event_detail.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.detail_event'


class EventDeleteView(RedirectPermissionRequiredMixin, DeleteView):
    template_name = 'event_delete_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.delete_event'
    success_message = "Event deleted successfully."
    success_url = reverse_lazy('events:eventDelete')
