from django.shortcuts import render
from django.core.mail import send_mail # for mail send we need to import it
from .models import Service

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def components(request):
    return render(request, 'components.html', {})


