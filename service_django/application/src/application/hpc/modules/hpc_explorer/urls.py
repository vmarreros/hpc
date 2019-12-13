# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^list/$', view=views.ls, name='list'),

    url(regex=r'^edit/$', view=views.edit, name='edit'),
    url(regex=r'^rename/$', view=views.rename, name='rename'),
    url(regex=r'^download/$', view=views.download, name='download'),
    url(regex=r'^paste/$', view=views.paste, name='paste'),
    url(regex=r'^execute/$', view=views.execute, name='execute'),
    url(regex=r'^delete/$', view=views.delete, name='delete'),

    url(regex=r'^go-to/$', view=views.go_to, name='go-to'),
    url(regex=r'^create-folder/$', view=views.create_folder, name='create-folder'),
    url(regex=r'^create-file/$', view=views.create_file, name='create-file'),
    url(regex=r'^upload/$', view=views.upload, name='upload'),

    url(regex=r'^error/$', view=views.error, name='error'),
]
