from django.shortcuts import render
from core.models import Event


# Create your views here.


def list_events(request):
    events = Event.objects.all()
    response = {'events': events}
    return render(request, 'agenda.html', response)

