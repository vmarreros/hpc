# -*- coding: utf-8 -*-
from django import template

from src.application.help import models

register = template.Library()


@register.filter()
def deep(instance):
    deep = ""
    while instance.parent:
        deep += "&nbsp;&nbsp;&nbsp;"
        instance = models.Document.objects.get(pk=instance.parent)
    return deep
