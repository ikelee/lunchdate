from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def landing_admin(request):
    return render(request, 'landing_admin.html')

def landing_member(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        log_in(request, user)
        return render(request, 'landing_member.html')
    else:
        return render(request, 'index.html')

def billing(request):
    return render(request, 'billing.html')

def session_detail(request):
    return render(request, 'session_detail.html')

def member_status(request):
    return render(request, 'member_status.html')

def set_up_new_user_host(request):
    return render(request, 'new_host.html')

def set_up_new_user_participant(request):
    return render(request, 'new_participant.html')