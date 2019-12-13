# -*- coding: utf-8 -*-
from . import views
from .modules.hpc_explorer import views as v
from django.conf.urls import include, url

urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^index___load/$', view=views.index___load, name='index___load'),
    url(regex=r'^index___title/$', view=views.index___title, name='index___title'),
    url(regex=r'^index___header/$', view=views.index___header, name='index___header'),
    url(regex=r'^index___leftside/$', view=views.index___leftside, name='index___leftside'),
    url(regex=r'^index___content___center/$', view=views.index___content___center, name='index___content___center'),
    url(regex=r'^index___content___footer/$', view=views.index___content___footer, name='index___content___footer'),
    url(regex=r'^download/$', view=v.download, name='download'),
    #
    url(regex=r'^login/$', view=views.login, name='login'),
    url(regex=r'^login___forgot_credentials_1/$', view=views.login___forgot_credentials_1, name='login___forgot_credentials_1'),
    url(regex=r'^login___forgot_credentials_2/(?P<pk>\d+)/$', view=views.login___forgot_credentials_2, name='login___forgot_credentials_2'),
    url(regex=r'^login___forgot_credentials_3/(?P<pk>\d+)/$', view=views.login___forgot_credentials_3, name='login___forgot_credentials_3'),
    url(regex=r'^login___request/$', view=views.login___request, name='login___request'),
    url(regex=r'^logout/$', view=views.logout, name='logout'),
    url(regex=r'^profile/$', view=views.profile, name='profile'),
    url(regex=r'^locale/$', view=views.locale, name='locale'),
    #
    url(r'^modules/', include('src.application.hpc.modules.urls', namespace='modules')),
]