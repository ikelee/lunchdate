from django.contrib.auth.models import User
from django.shortcuts import render

from lunchDateApp.models import Session_Host, Session_Participant
import datetime

from enum import Enum

class User_Type(Enum):
    HOST = 1
    PARTICIPANT = 2

def create_new_user(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.save()
    return render(request, 'signup_detail.html', {'host': User_Type.HOST, 'participant': User_Type.PARTICIPANT})

def new_host_detail(request):
    session_host = Session_Host(host_name=request.POST['host_name'], created_date=datetime.datetime.now())
    session_host.save()
    return render(request, 'landing_host.html')

def new_participant_detail(request):
    try: 
        host = Session_Host.objects.filter(host_name=request.POST['session_host']).first()
    except Session_Host.ObjectDoesNotExist:
        print("Not found")
        host = None 
 
    session_participant = Session_Participant(
        participant_name=request.POST['participant_name'], 
        session_host=host,
        created_date=datetime.datetime.now(),
        participant_age=request.POST['participant_age'],
        participant_team=request.POST['participant_team'],
        participant_location_index=request.POST['participant_location_index']
        )
    session_participant.save()
    return render(request, 'landing_participant.html')
