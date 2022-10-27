from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="confirm pass",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        emaile = self.cleaned_data['email']
        user = User.objects.filter(email=emaile).exists()
        if user:
            raise ValidationError('in email tekrarist')
        return emaile

    def clean_name(self):
        namee = self.cleaned_data['name']
        user = User.objects.filter(username=namee).exists()
        if user:
            raise ValidationError('in user tekrarist')
        return namee

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('pass not shabih')


class UserLoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('age', 'bio')
