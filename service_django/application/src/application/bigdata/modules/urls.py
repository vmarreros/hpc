# -*- coding: utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^bigdata_module01/', include('src.application.bigdata.modules.bigdata_module01.urls', namespace='bigdata_module01')),
]
