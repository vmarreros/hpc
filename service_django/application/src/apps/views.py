from django import shortcuts
from django.urls import reverse


def index(request):
    return shortcuts.redirect(reverse('website:index'))
