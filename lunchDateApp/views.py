from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def landing_admin(request):
    return render(request, 'landing_admin.html')

def landing_member(request):
    return render(request, 'landing_member.html')

def billing(request):
    return render(request, 'billing.html')

def session_detail(request):
    return render(request, 'session_detail.html')

def member_status(request):
    return render(request, 'member_status.html')
