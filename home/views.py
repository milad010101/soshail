from distutils.core import setup
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Coments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .form import UpdateCratePostForm, CommentForm
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    def get(self, request):
        post = Post.objects.all()

        return render(request, 'home/index.html', {'post': post})


class DetailPoatView(View):
    class_form = CommentForm

    def setup(self, request, *args, **kwargs):
        self.post_inctance = get_object_or_404(
            Post, id=kwargs['id_post'], slug=kwargs['slug_post'])

        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        comments = self.post_inctance.post_comment.filter(is_reply=False)
        return render(request, 'home/detail.html', {'post': self.post_inctance, 'comments': comments, 'class_form': self.class_form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.class_form(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.post = self.post_inctance
            new_form.save()
            messages.success(request, 'you message post success', 'success')
        return redirect('detail', self.post_inctance.id, self.post_inctance.slug)


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
    form_class = UpdateCratePostForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = Post.objects.get(id=kwargs['id_post'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.post_instance
        if not post.user.id == request.user.id:
            messages.warning(
                request, 'you  cant update post', 'warning')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id_post):
        post = self.post_instance
        form = self.form_class(instance=post)
        return render(request, 'home/update.html', {'form': form})

    def post(self, request, id_post):
        post = self.post_instance
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.save()
            messages.success(
                request, 'you update post success', 'success')
            return redirect('detail', post.id, post.slug)


class CreatePostViwe(LoginRequiredMixin, View):
    form_class = UpdateCratePostForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'home/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save()
            messages.success(
                request, 'you create post success', 'success')
            return redirect('detail', new_post.id, new_post.slug)
