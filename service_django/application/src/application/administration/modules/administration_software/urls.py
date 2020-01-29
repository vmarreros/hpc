# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('installed/', include(('src.application.administration.modules.administration_software.installed.urls', app_name), namespace='installed')),
    path('requested/', include(('src.application.administration.modules.administration_software.requested.urls', app_name), namespace='requested')),
]
