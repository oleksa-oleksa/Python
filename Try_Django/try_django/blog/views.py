from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost

def blog_post_detail_page(request, post_id):
    print(post_id.__class__)
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

