# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Module, Version


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'module',)
    search_fields = ('name', 'module',)
