# Model View Template
# Whatever we want to change a page we start with a view
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    # doc = "<h1> Hello {title}</h1".format(title=title)
    # two curly brackets for django rendered document
    # django_rendered_doc = "<h1> Hello {{title}}</h1".format(title=title)
    title = "Hello there...."

    qs = BlogPost.objects.all().published()[:5]

    context = {"title": "Welcome to Try Django", 'blog_list': qs}
    return render(request, "index.html", context)


def about_page(request):
    content = {"title" : "About page"}
    template_name = "about.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(content)

    return HttpResponse(rendered_item)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
                "title": "Contact us",
                "form": form
    }
    return render(request, "form.html", context)



