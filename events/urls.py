from django.urls import path

from events.views import CalendarView, EventsListView
app_name = 'events'

urlpatterns = [
  path('calendar/',CalendarView.as_view(), name='calendar'),
  path('events_list/',EventsListView.as_view(), name='eventslist'),
]