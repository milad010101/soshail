from django.shortcuts import render, redirect
from django.views import View
from .form import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


class Register(View):
    class_Form = RegisterForm

    def get(self, request):
        forms = self.class_Form()
        return render(request, 'acount/register.html', {'forms': forms})

    def post(self, request):
        forms = self.class_Form(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            User.objects.create_user(cd['name'], cd['email'], cd['password'])
            messages.success(request, 'user crated', 'success')
            return redirect('home')
        return render(request, 'acount/register.html', {'forms': forms})
