from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginuser')
    context = {'registerform' : form}
    return render(request, 'accounts/register.html', context = context)


def loginuser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate (request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {'loginForm': form}
    return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')
