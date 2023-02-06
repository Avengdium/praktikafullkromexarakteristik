from django import forms
from django.contrib.auth.models import User
from urllib import request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm, LoginForm, ProfileUpdateForm, UserUpdateForm
from users.models import Profile

def register(request):
    error = ""
    if request.method == 'POST': #if the form has been submitted
        form = UserRegisterationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
        else:
            error = "Форма заполнена некорректно"
    form = UserRegisterationForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'users/register.html', data)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
              
    form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def profile(request):
    us = request.user

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'us': us
    }

    return render(request, 'users/profile.html', context)

def user_logout(request):
    logout(request)
    
    return render(request,'users/logout.html')