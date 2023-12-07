from django.shortcuts import render

def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def property(request):
    return render(request,"properties.html")
def details(request):
    return render(request,"property-details.html")