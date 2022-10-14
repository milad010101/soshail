from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Post


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)