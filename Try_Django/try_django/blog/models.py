from django.db import models

# Create your models here.
class BlogPost(models.Model):
    # id = PrimaryKey, Integer
    title = models.TextField()
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
