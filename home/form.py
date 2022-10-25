from dataclasses import field, fields
from pyexpat import model
from xml.dom.minidom import Comment
from django import forms
from .models import Post, Coments


class UpdateCratePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ('body',)


class SerchForm(forms.Form):
    serch = forms.CharField()
