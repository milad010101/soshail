from enum import auto
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    createf = models.DateTimeField()
    updted = models.DateTimeField()

    def __str__(self):
        return self.slug
