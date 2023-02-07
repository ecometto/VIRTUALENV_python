from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index2(request):
    return HttpResponse('hello from index2')