from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            args["user"] = user
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'authorization/login.html', args)
    else:
        return render(request, 'authorization/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")
