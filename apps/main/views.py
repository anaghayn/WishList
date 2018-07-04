# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

def index(request):
    return render(request, 'main/index.html')

def register(request):
    name=request.POST['first_name']
    email=request.POST['email']
    username=request.POST['u_name']
    password=request.POST['password']
    confirm_pswd=request.POST['confirm']
    hired=request.POST['date_hired']
    valid=True
    if len(name)<2:
        valid=False
        messages.add_message(request,messages.ERROR,'Please enter valid name')
    if len(username)<2:
        valid=False
        messages.add_message(request,messages.ERROR,'Please enter valid email')
    if len(password)<8:
        valid=False
        messages.add_message(request,messages.ERROR,'password must be at least 8 characters')
    if password != confirm_pswd:
        valid=False
        messages.add_message(request,messages.ERROR,'Password do not match')
    
    if valid == True: 
        user = User.objects.create(name=name, email=email, password=password, username=username, hired_date=hired)
        request.session['user_id']=user.id
        request.session['username']=user.username
        messages.add_message(request,messages.Success,'Successfully registered..!!')
        return redirect('home:home') 
    else:
        return redirect("user:home")

def login(request):
    username=request.POST['u_name']
    password=request.POST['password']
    #confirm_pswd=request.POST['confirm']
    valid = True
    #if password != confirm_pswd:
    #    valid=False
    #    messages.add_message(request,messages.ERROR,'Password do not match')
    if len(username)<2:
        valid=False
        messages.add_message(request,messages.ERROR,'Please enter valid email')
    if valid == True:
        user = User.objects.get(username = username)
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        return redirect('home:home')
    else:
        messages.add_message(request,messages.ERROR,'Invalid login. Please check your Username and Password')
        return redirect('user:home')

def logout(request):
    request.session.clear()
    return redirect("user:home")                      
   
# Create your views here.
