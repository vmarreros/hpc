# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^website_home/', include('src.application.website.modules.website_home.urls', namespace='website_home')),
]
