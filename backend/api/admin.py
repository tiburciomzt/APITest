from sys import implementation
from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    
admin.site.register(BlogPost)