from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from core.models import Event


# Create your views here.

def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            messages.error(request, "User or password invalid")

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def list_events(request):
    events = Event.objects.all()
    response = {'events': events}
    return render(request, 'agenda.html', response)


@login_required(login_url='/login')
def event(request):
    event_id = request.GET.get('id')
    data = {}
    if event_id:
        data['event'] = Event.objects.get(id=event_id)

    return render(request, 'event.html', data)


@login_required(login_url='/login')
def submit_event(request):
    if request.POST:
        title = request.POST.get('title')
        event_date = request.POST.get('event_date')
        description = request.POST.get('description')
        user = request.user
        event_id = request.POST.get('event_id')

        if event_id:
            user_event = Event.objects.get(id=event_id)

            if user_event.user == user:
                user_event.title = title
                user_event.description = description
                user_event.event_date = event_date
                user_event.save()
        else:
            Event.objects.create(
                title=title,
                event_date=event_date,
                description=description,
                user=user
            )

    return redirect('/')


@login_required(login_url='/login')
def delete_event(request, event_id):
    user = request.user
    user_event = Event.objects.get(id=event_id)

    if user == user_event.user:
        user_event.delete()

    return redirect('/')
