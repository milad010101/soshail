from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Relaship(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    user_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.from_user}folow mikone {self.user_to}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(null=True, blank=True)
