from ast import Not
from email import message
from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from home import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import UpdatePostForm


class Home(View):
    def get(self, request):
        post = Post.objects.all()

        return render(request, 'home/index.html', {'post': post})


class DetailPoatView(View):
    def get(self, request, id_post, slug_post):
        post = Post.objects.get(id=id_post, slug=slug_post)
        return render(request, 'home/detail.html', {'post': post})


class DeletePostViwe(LoginRequiredMixin, View):
    def get(self, request, id_post):
        post = Post.objects.get(id=id_post)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'you delete post success', 'success')
        else:
            messages.warning(
                request, 'you  cant delete post success', 'warning')
        return redirect('home')


class UpdatePostViwe(LoginRequiredMixin, View):
    form_class = UpdatePostForm

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['id_post'])
        if not post.user.id == request.user.id:
            messages.warning(
                request, 'you  cant update post', 'warning')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_post):
        post = Post.objects.get(id=id_post)
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form': form})

    def post(self, request):
        pass
