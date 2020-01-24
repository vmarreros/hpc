# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^history/$', view=views.history, name='history'),
    url(regex=r'^history_json/$', view=views.history_json, name='history_json'),
    url(regex=r'^queue/$', view=views.queue, name='queue'),
    url(regex=r'^queue_json/$', view=views.queue_json, name='queue_json'),
    url(regex=r'^detail_job/$', view=views.detail_job, name='detail_job'),
    url(regex=r'^action_job/$', view=views.action_job, name='action_job')
]
