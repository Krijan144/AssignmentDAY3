from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def welcome(request):
    x='WELCOME'
    d={
        'date':x
    }
    return render(request, 'home.html', d)

def today(request):
 x = datetime.datetime.now()
 d={
    'date':x
 }
 return render(request,'home.html',d)

def timestamp(request):
    ts = ts = datetime.datetime.now().timestamp()
    d={
        'date':ts
        
    }
    return render(request, 'home.html', d)