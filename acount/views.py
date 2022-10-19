from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from .form import RegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from .models import Relaship


class Register(View):
    class_Form = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        forms = self.class_Form()
        return render(request, 'acount/register.html', {'forms': forms})

    def post(self, request):
        forms = self.class_Form(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            User.objects.create_user(cd['name'], cd['email'], cd['password1'])
            messages.success(request, 'user crated', 'success')
            return redirect('home')
        return render(request, 'acount/register.html', {'forms': forms})


class UserLoginViwe(View):
    Form_class = UserLoginForm

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.Form_class()
        return render(request, 'acount/login.html', {'form': form})

    def post(self, request):
        form = self.Form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['name'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'your login sucsses', 'success')
                if self.next:
                    return redirect('self.next')
                return redirect('home')
            messages.error(request, 'your pass and user not', 'warning')
        return render(request, 'acount/login.html', {'form': form})


class UserLogoutViwe(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, 'yuor logout account success ', 'success')

        return redirect('login')


class ProfileViwe(LoginRequiredMixin, View):

    def get(self, request, user_id):
        this_follow = False

        user = User.objects.get(id=user_id)
        post = user.posts.all()
        relship = Relaship.objects.filter(
            from_user=request.user, user_to=user)
        if relship.exists():
            this_follow = True

        return render(request, 'acount/profile.html', {'user': user, 'post': post, 'request': request, 'this_follow': this_follow})


class ResetPaswordView(auth_view.PasswordResetView):
    template_name = 'acount/FormEmail.html'
    success_url = reverse_lazy('success_url_done')
    email_template_name = 'acount/emailtemp.html'


class UserPaswordDoneView(auth_view.PasswordResetDoneView):
    template_name = 'acount/pasworddone.html'


class UserPaswordConfirmView(auth_view.PasswordResetConfirmView):
    template_name = 'acount/paswordconfirm.html'
    success_url = reverse_lazy('pasword_compelete')


class UserPaswordCompeleteView(auth_view.PasswordResetCompleteView):
    template_name = 'acount/paswordcompelete.html'


class FollowView(LoginRequiredMixin, View):
    def get(self, request, id_user):
        user = User.objects.get(id=id_user)
        relship = Relaship.objects.filter(
            from_user=request.user, user_to=user)
        if relship.exists():
            messages.error(request, 'شما قبلا فالو کردید', 'error')
        else:
            Relaship.objects.create(from_user=request.user, user_to=user)
            messages.success(request, 'شما فالو کردید', 'success')
        return redirect('profile', user.id)


class UnFollowView(LoginRequiredMixin, View):
    def get(self, request, id_user):
        user = User.objects.get(id=id_user)
        relship = Relaship.objects.filter(
            from_user=request.user, user_to=user)
        if relship.exists():
            relship.delete()
            messages.success(request, 'شما آنفالو کردید', 'success')
        else:
            messages.error(request, 'شما اصلا فالو نکردید', 'error')
        return redirect('profile', user.id)
