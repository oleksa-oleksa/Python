from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # BlogPost objects
        return self.filter(publish_date__lte=now)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)


# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset
    # id = PrimaryKey, Integer
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.FileField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    '''Any information that is “not a form Field” can be considered as metadata. 
    Django provides sensible defaults to all fields. But if you want to override 
    the default behavior of fields, you can define the corresponding meta options. 
    '''
    class Meta:
        ordering = ['publish_date', '-updated_date', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"