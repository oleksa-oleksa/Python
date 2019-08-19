from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    conten = models.TextField(null=True, blank=True)



class Blog:
    title = "Hello world"
    content = "something cool"