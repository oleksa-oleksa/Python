from django.db import models


# Create your models here.
class BlogPost(models.Model):
    # id = PrimaryKey, Integer
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
