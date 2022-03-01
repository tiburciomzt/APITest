from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import BlogPost

class UserSerializer(serializers.HyperlinkedModelSerializer):
    model = User
    fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id','src', 'program', 'title', 'date', 'description', 'system')