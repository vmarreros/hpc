# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'website'

urlpatterns = [
    path('website_home/', include(('src.application.website.modules.website_home.urls', app_name), namespace='website_home')),
]
