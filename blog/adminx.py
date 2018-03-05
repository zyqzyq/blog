# -*- coding: utf-8 -*-
import xadmin

__author__ = "zyqzyq"
__time__ = '2018/3/5 13:50'
from django.db import models
from .models import Tag, Category, Post
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
class PostAdmin(object):
    list_display = ['title', 'created_time', 'modified_time', "category", 'author']
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


xadmin.site.register(Tag)
xadmin.site.register(Category)
xadmin.site.register(Post, PostAdmin)
