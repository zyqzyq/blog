# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from .models import Tag, Category, Post
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', "category", 'author']
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
