# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.db import models
from ..main.models import *

class Item(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, related_name='items')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Wish(models.Model):
    wish=models.ForeignKey(Item, related_name='wishers')
    wisher=models.ForeignKey(User, related_name='wishes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


# Create your models here.
