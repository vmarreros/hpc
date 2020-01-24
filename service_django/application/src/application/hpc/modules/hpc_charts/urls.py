# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^nodes/$', view=views.nodes, name='nodes'),
    url(regex=r'^nodes_json/$', view=views.nodes_json, name='nodes_json'),
    url(regex=r'^jobs/$', view=views.jobs, name='jobs'),
    url(regex=r'^users/$', view=views.users, name='users'),
]
