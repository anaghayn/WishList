# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
from ..main.models import *
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        user=request.session['user_id']
        context={
            'items': Item.objects.exclude(wishers__wisher_id=user),
            'wishes': Wish.objects.filter(wisher_id=user),
            'all': Wish.objects.all()
        }
    return render(request,'WL/index.html', context)

def addItem(request):
    if request.method == "POST":
        wish = request.POST['wish_name']
        if len(wish)>3:
            items= Item.objects.create(title= wish, user_id=request.session['user_id'])
            Wish.object.create(wish_id= items.id, wisher_id = request.session['user_id'])
        return redirect('home:home')
    else:
        messages.add_message(request, messages.ERROR, 'Item should be at least 3 characters')
    return redirect('home:addItem')
    return render(request, 'WL/addItem.html')

def addWish(request):
    Wish.objects.create(wish_id= wish_id, wisher_id= request.session['user_id'])
    return redirect('home:home')

def removeWish(request):
    Wish.objects.get(wish_id= wish_id, wisher_id= request.session['user_id']).delete()
    return redirect('home:home')

def item(request):
    context={
        'item' : Item.objects.get(id = item_id),
        'wish' : Wish.objects.filter(wish_id = item_id)
    }
    return render(request, 'WL/item.html', context)

def delete(request):
    Item.objects.get(id= item_id, user_id= request.session['user_id']).delete()
    return redirect('home:home')

# Create your views here.
