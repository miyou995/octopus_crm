from django.urls import path
from django.contrib.auth.decorators import login_required
from events.views import CalendarView, EventsListView, EventCreateView, EventDeleteView, EventDetailView, EventUpdateView
app_name = 'events'

urlpatterns = [
  path('calendar/',CalendarView.as_view(), name='calendar'),
  path('eventlist/',login_required(EventsListView.as_view()), name='eventlist'),
  path('eventcreate/',login_required(EventCreateView.as_view()), name='eventcreate'),
  path('eventedit/<int:pk>',login_required(EventUpdateView.as_view()), name='eventedit'),
  path('eventdelete/<int:pk>',login_required(EventDeleteView.as_view()), name='eventdelete'),
  path('eventdetail/<int:pk>',login_required(EventDetailView.as_view()), name='eventdetail'),
]