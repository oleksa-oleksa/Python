# Model View Template
# Whatever we want to change a page we start with a view
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "Oleksandra Baga"
    #doc = "<h1> Hello {title}</h1".format(title=title)
    # two curly brackets for django rendered document
    #django_rendered_doc = "<h1> Hello {{title}}</h1".format(title=title)
    return render(request, "index.html", {"title": title})


def about_page(request):
    return render(request, "index.html", {"title": "I am a student and I live in Berlin"})


def contact_page(request):
    return render(request, "index.html", {"title": "Don't hesitate to contact me!"})



