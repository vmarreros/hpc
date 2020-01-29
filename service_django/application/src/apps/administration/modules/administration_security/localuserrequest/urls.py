# -*- coding: utf-8 -*-
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list/', view=views.list, name='list'),
    re_path(r'^detail/(?P<pk>\d+)/$', view=views.detail, name='detail'),
    re_path(r'^approve/(?P<pk>\d+)/$', view=views.approve, name='approve'),
    re_path(r'^disapprove/(?P<pk>\d+)/$', view=views.disapprove, name='disapprove'),
]
