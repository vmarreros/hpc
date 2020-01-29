# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('history/', view=views.history, name='history'),
    path('history_json/', view=views.history_json, name='history_json'),
    path('queue/', view=views.queue, name='queue'),
    path('queue_json/', view=views.queue_json, name='queue_json'),
    path('detail_job/', view=views.detail_job, name='detail_job'),
    path('action_job/', view=views.action_job, name='action_job')
]
