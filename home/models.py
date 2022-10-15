from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    createf = models.DateTimeField()
    updted = models.DateTimeField()

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('detail', args=(self.id, self.slug))
