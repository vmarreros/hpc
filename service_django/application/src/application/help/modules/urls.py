# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'modules'

urlpatterns = [
    path('help_document/', include('src.application.help.modules.help_document.urls', namespace='help_document')),
]
