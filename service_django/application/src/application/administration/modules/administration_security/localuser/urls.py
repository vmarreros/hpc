# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^list/$', view=views.list, name='list'),
    url(regex=r'^create/$', view=views.create, name='create'),
    url(regex=r'^detail/(?P<pk>\d+)/$', view=views.detail, name='detail'),
    url(regex=r'^update/(?P<pk>\d+)/$', view=views.update, name='update'),
    url(regex=r'^delete/(?P<pk>\d+)/$', view=views.delete, name='delete'),
]
