from dataclasses import fields
from pydoc import classname
from pyexpat import model
from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('src', 'program', 'title', 'date',
        'description', 'system')