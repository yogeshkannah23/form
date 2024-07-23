from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from form_app.models import *
# Create your views here.

def index(request):
    return HttpResponse("Index page")
