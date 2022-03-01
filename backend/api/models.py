from django.db import models


class BlogPost(models.Model):
    src = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    system = models.CharField(max_length=30, blank=True, null=True)
 