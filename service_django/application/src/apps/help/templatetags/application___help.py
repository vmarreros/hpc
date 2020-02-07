from django import template

from src.apps.help import models

register = template.Library()


@register.filter()
def deep(instance):
    deep = ""
    while instance.parent:
        deep += "&nbsp;&nbsp;&nbsp;"
        instance = models.Document.objects.get(pk=instance.parent)
    return deep
