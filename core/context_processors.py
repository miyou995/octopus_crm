from django.shortcuts import render , get_object_or_404
from events.models import Event

def infos(request):
    event = Event.objects.all()
    return {
            'events' : event,
            # 'start_date' : event,
        }
    

