# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('document/', include(('src.application.administration.modules.administration_help.document.urls', app_name), namespace='document')),
]
