# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name= models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 255)
    hired_date = models.DateField(auto_now_add= True)
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now=True)

# Create your models here.
