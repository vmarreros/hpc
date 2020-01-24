# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^help_document/', include('src.application.help.modules.help_document.urls', namespace='help_document')),
]
