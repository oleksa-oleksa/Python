from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(request, post_id):
    try:
        obj = BlogPost.objects.get(id=post_id)
    except:
        raise Http404
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

