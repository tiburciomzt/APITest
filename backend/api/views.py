import imp
from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView , ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import BlogPost
from .serializers import PostViewSerializer, UserSerializer, GroupSerializer


class PostView(viewsets.ModelViewSet):
    serializer_class = PostViewSerializer
    queryset = BlogPost.objects.all()

class IndexView(TemplateView):
    template_name = 'index.html'