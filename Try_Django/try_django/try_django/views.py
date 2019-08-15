# Model View Template
# Whatever we want to change a page we start with a view
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "index.html")


def about_page(request):
    return HttpResponse("<h1>I am Oleksa</h1>")


def contact_page(request):
    return HttpResponse("<h1>Write me and hire me! Give me money!</h1>")


