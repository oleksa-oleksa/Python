from django.contrib import admin

# Register your models here.
from .models import SearchQuery
admin.site.register(SearchQuery)