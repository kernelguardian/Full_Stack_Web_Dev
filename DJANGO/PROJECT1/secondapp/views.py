from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'insert_me':"This is from views.py"}
    return render(request,'secondapp/help.html',context=my_dict)
