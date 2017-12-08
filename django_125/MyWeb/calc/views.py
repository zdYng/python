from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR #项目目录

# Create your views here.
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) +int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request,'home.html')
def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )

def jsondata(request):
    return render(request,'test_data.json')