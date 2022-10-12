from django.shortcuts import render, redirect
from django.views import View
from .form import RegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


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
                return redirect('home')
            messages.error(request, 'your pass and user not', 'warning')
        return render(request, 'acount/login.html', {'form': form})


class UserLogoutViwe(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'yuor logout account success ', 'success')

        return redirect('home')
