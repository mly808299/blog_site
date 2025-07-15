from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html')
        else:
            return render(request, 'account/login.html')
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('home:home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return redirect('account/register.html')
        user = User.objects.create_user(username=username, password=password )
        login(request, user)
        return redirect('home:home')
    return render(request, 'account/register.html')
