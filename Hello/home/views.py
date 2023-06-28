from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("This is aboutpage")

def services(request):
    return HttpResponse("This is service page")

def contact(request):
    return HttpResponse("This is contact page")