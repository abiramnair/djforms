from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def SuccessView(request):
    return HttpResponse('Your form was submitted successfully')


def LoginView(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            message = 'that username or password was incorrect'
            return render(request, 'formsandbox/login.html', {'form': form, 'message': message})
    return render(request, 'formsandbox/login.html', {'form': form})
