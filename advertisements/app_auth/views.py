from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/profile.html', {'error': 'Пользователь не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.save()
            return render(request, 'app_auth/register.html', {'user': user})
    else:
        register_form = RegisterForm()
    return render(request, 'app_auth/register.html', {'register_form': register_form})