from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("<h1>Hello World</h1>")


