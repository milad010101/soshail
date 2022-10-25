from ast import NameConstant
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    create = models.DateTimeField()
    updted = models.DateTimeField()

    class Meta:
        ordering = ['create']

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('detail', args=(self.id, self.slug))

    def Count_Lile(self):
        return self.plike.count()


class Coments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comment')
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='reply_comment', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=400)

    def __str__(self):
        return f'{self.user}-{self.body[:30]}'


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ulike')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='plike')

    def __str__(self):
        return f'{self.user}like to {self.post}'
