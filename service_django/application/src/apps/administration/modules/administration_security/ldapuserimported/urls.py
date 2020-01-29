# -*- coding: utf-8 -*-
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list/', view=views.list, name='list'),
    re_path(r'^detail/(?P<pk>\d+)/$', view=views.detail, name='detail'),
    re_path(r'^update/(?P<pk>\d+)/$', view=views.update, name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', view=views.delete, name='delete'),
]
