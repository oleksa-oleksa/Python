# Model View Template
# Whatever we want to change a page we start with a view
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    title = "Oleksandra Baga"
    #doc = "<h1> Hello {title}</h1".format(title=title)
    # two curly brackets for django rendered document
    #django_rendered_doc = "<h1> Hello {{title}}</h1".format(title=title)
    return render(request, "index.html", {"title": title})


def about_page(request):
    content = {"title" : "About page"}
    template_name = "about.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(content)

    return HttpResponse(rendered_item)


def contact_page(request):
    return render(request, "index.html", {"title": "Don't hesitate to contact me!"})



