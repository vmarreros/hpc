# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^installed/$', view=views.installed, name='installed'),
    url(regex=r'^request_software$', view=views.request_software, name='request_software'),
]
