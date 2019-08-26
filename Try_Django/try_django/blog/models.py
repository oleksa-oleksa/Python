from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset
    # id = PrimaryKey, Integer
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
