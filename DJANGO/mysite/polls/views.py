from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World, You are now at polls apps views.py")

# Create your views here.
