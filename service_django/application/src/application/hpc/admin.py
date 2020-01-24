# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SoftwareInstalled, SoftwareVersion, SoftwareRequested


@admin.register(SoftwareInstalled)
class SoftwareInstalledAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(SoftwareVersion)
class SoftwareVersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version', 'software',)
    search_fields = ('version', 'software',)


@admin.register(SoftwareRequested)
class SoftwareRequestedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'software', 'website', 'version', 'type', 'installation_guide', 'motivation', 'account')
    # search_fields = ('software',)
