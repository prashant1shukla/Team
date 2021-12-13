from django.shortcuts import render
from datetime import datetime
from home.models import Details

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'login.html')
    

def index(request):

    dests = Details.objects.all()

    return render(request, "index.html", {'dests': dests})
    