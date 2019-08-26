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

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title=title)
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title
