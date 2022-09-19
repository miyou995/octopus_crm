from django.urls import path

from events.views import CalendarView
app_name = 'events'

urlpatterns = [
  path('calendar/',CalendarView.as_view(), name='calendar'),
    
]