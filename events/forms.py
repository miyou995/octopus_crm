from multiprocessing import Event
from django.forms import ModelForm
from .models import Event

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'