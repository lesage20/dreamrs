from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
# Create your views here.

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'incorrect datas')
        
    
    datas = {
        
    }
    return render(request, 'login.html', datas)

def log_out(request):
    logout(request)
    return redirect('login')


def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
        
    
    datas = {
        'form': form
    }
    
    return render(request, 'register.html', datas)

def forgot(request):
    datas = {
        
    }
    return render(request, 'forgot-password.html', datas)
