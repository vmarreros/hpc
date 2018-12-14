# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^document/', include('src.application.administration.modules.administration_home.document.urls', namespace='document')),
]
