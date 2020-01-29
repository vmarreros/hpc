# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'modules'

urlpatterns = [
    path('bigdata_module01/', include('src.application.bigdata.modules.bigdata_module01.urls', namespace='bigdata_module01')),
]
