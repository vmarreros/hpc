# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('installed/', view=views.installed, name='installed'),
    path('request_software', view=views.request_software, name='request_software'),
]
