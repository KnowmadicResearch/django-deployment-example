from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse('home sweet home')