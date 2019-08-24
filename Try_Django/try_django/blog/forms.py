from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    # to change the form instead of model 
    # title = forms.CharField(max_length=150)
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content"]
