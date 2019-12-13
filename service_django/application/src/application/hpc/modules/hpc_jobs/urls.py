# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^list/$', view=views.jobs, name='list'),
    url(regex=r'^detail/$', view=views.detail, name='detail'),
    url(regex=r'^action/$', view=views.action, name='action'),
]
