from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1": "Somya is learning python",
        "variable2": "Somya is learning django"
    }

    return render(request , "index.html" , context)
    #return HttpResponse("This is homepage")

def about(request):
    #return HttpResponse("This is aboutpage")
    return render(request, "about.html")

def services(request):
    #return HttpResponse("This is service page")
    return render(request, "services.html")

def contact(request):
    #return HttpResponse("This is contact page")
    return render(request, "contact.html")