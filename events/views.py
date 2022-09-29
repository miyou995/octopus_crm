from datetime import date
import json
from multiprocessing import context
from unittest import result
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
from .choice import EVENT_PRIORITY, TICKET_STATUTE_TYPES
from .models import Event
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ValidationError



class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())

class CalendarView(TemplateView):
    template_name = "calendar.html" 
    form_class = AddEventForm

    # def event(request):
    #     all_events = Event.objects.all()
    # # get_event_types = Events.objects.only('event_category')

    # # if filters applied then get parameter and filter based on condition else return object
    #     if request.GET:
    #         event_arr = []
    #         # if request.GET.get('event_category') == "all":
    #         #     all_events = Events.objects.all()
    #         # else:
    #         #     all_events = Events.objects.filter(event_category__icontains=request.GET.get('event_category'))

    #         for i in all_events:
    #             event_sub_arr = {}
    #             event_sub_arr['title'] = i.event_subject
    #             start_date = date(i.start_date.date(), "%Y-%m-%d")
    #             end_date = date(i.deadline.date(), "%Y-%m-%d")
    #             event_sub_arr['start'] = start_date
    #             event_sub_arr['end'] = end_date
    #             event_arr.append(event_sub_arr)
    #         return HttpResponse(json.dumps(event_arr))

    #     # context = {
    #     #     "events":all_events,
    #     #     # "get_event_types":get_event_types,
    #     #     }
    #     return render(request,'calendar',context)

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        context["eventlist"] = Event.objects.all()
        context["eventpriorities"] = EVENT_PRIORITY
        # context[]


        return context


class EventsListView(RedirectPermissionRequiredMixin, ListView):
    template_name = "events_list.html" 
    model = Event
    # form_class = AddEventForm
    permission_required = 'events.view_event'

    def get_context_data(self, **kwargs):
        context = super(EventsListView, self).get_context_data(**kwargs)
        # event_id = self.get_object().id
        context["events"] = Event.objects.order_by('start_date', 'start_time')
        context["eventpriorities"] = EVENT_PRIORITY

        return context

class EventCreateView(RedirectPermissionRequiredMixin, CreateView):
    template_name = 'event_create_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.create_event'
    success_message = "Event created successfully."
    success_url = reverse_lazy('events:eventlist')

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        context["eventpriorities"] = EVENT_PRIORITY

        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.as_text())
        result = redirect("events:eventlist")
        return result

        # try:
        #     result = redirect("events:eventlist")
        # except:
        #     raise
        # else:
        #     return result
    



class EventUpdateView(RedirectPermissionRequiredMixin, UpdateView):
    template_name = 'event_edit_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.edite_event'
    success_message = "Event updated successfully."
    success_url = reverse_lazy('events:eventlist')

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context["eventpriorities"] = EVENT_PRIORITY
        return context

    def form_invalid(self, form):
        messages.error(self.request, form.errors.as_text())
        return redirect("events:eventlist")

    # def form_invalid(self, form):

    #     messages.error(self.request, form.errors.as_text())
    #     # return redirect("events:eventlist")

    #     # messages.add_message(self.request, messages.ERROR, form.errors)
    #     # result = redirect("events:eventlist")
    #     try:
    #         result = redirect("events:eventlist")
    #         return result
    #     # except:
    #     #     raise
    #     # else:
    #     #     return result

    #     except ValidationError as err:
    #         if str(err) == "End date cannot be smaller then start date.":
    #             raise IntegrityError ("enter a corect date")
    #         raise
    #     else:
    #         # result = redirect("events:eventlist")
    #         return result

        # return result



class EventDetailView(RedirectPermissionRequiredMixin, DetailView):
    template_name = 'event_detail.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.detail_event'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context["eventpriorities"] = EVENT_PRIORITY

        return context


class EventDeleteView(RedirectPermissionRequiredMixin, DeleteView):
    template_name = 'event_delete_model.html'
    form_class = AddEventForm
    model = Event
    permission_required = 'event.delete_event'
    success_message = "Event deleted successfully."
    success_url = reverse_lazy('events:eventlist')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Error: the element has not been deleted")
        return redirect('envents:eventlist')

# class CalendarView(EventCreateView, TemplateView):
    template_name = "calendar.html" 
    form_class = AddEventForm

    def event(request):
        all_events = Event.objects.all()
    # get_event_types = Events.objects.only('event_category')

    # if filters applied then get parameter and filter based on condition else return object
        if request.GET:
            event_arr = []
            # if request.GET.get('event_category') == "all":
            #     all_events = Events.objects.all()
            # else:
            #     all_events = Events.objects.filter(event_category__icontains=request.GET.get('event_category'))

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.event_subject
                start_date = date(i.start_date.date(), "%Y-%m-%d")
                end_date = date(i.deadline.date(), "%Y-%m-%d")
                event_sub_arr['start'] = start_date
                event_sub_arr['end'] = end_date
                event_arr.append(event_sub_arr)
            return JsonResponse(event_arr)

        # context = {
        #     "events":all_events,
        #     # "get_event_types":get_event_types,
        #     }
        return render(request,'calendar',context)

    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        context["eventlist"] = Event.objects.all()

        return context
