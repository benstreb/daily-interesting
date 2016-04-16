from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    anchor = models.SlugField(max_length=100, null=True, unique=True)
    body = models.TextField()
