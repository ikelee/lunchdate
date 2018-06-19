from django.contrib.auth.models import User
from django.shortcuts import render

from lunchDateApp.models import Session_Host
from enum import Enum

class User_Type(Enum):
    HOST = 1
    PARTICIPANT = 2

def create_new_user(request):
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.save()
    return render(request, 'signup_detail.html', {'host': User_Type.HOST, 'participant': User_Type.PARTICIPANT, 'username': request.POST['username']})

def new_user_detail(request):
    session_host = Session_Host(host_name=request.POST['account_type'], created_date=request.POST['seat_count'])
    session_host.save()
    return render(request, 'login.html')