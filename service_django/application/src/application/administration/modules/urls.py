# -*- coding: utf-8 -*-
from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('administration_security/', include(('src.application.administration.modules.administration_security.urls', app_name), namespace='administration_security')),
    path('administration_software/', include(('src.application.administration.modules.administration_software.urls', app_name), namespace='administration_software')),
    path('administration_help/', include(('src.application.administration.modules.administration_help.urls', app_name), namespace='administration_help')),
]
