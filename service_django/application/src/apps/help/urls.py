# -*- coding: utf-8 -*-
from django.urls import path, re_path, include

from . import views

app_name = 'help'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('index___load/', view=views.index___load, name='index___load'),
    path('index___title/', view=views.index___title, name='index___title'),
    path('index___header/', view=views.index___header, name='index___header'),
    path('index___content___center/', view=views.index___content___center, name='index___content___center'),
    path('index___content___footer/', view=views.index___content___footer, name='index___content___footer'),
    #
    path('login/', view=views.login, name='login'),
    path('login___forgot_credentials_1/', view=views.login___forgot_credentials_1, name='login___forgot_credentials_1'),
    re_path(r'^login___forgot_credentials_2/(?P<pk>\d+)/$', view=views.login___forgot_credentials_2, name='login___forgot_credentials_2'),
    re_path(r'^login___forgot_credentials_3/(?P<pk>\d+)/$', view=views.login___forgot_credentials_3, name='login___forgot_credentials_3'),
    path('login___request/', view=views.login___request, name='login___request'),
    path('logout/', view=views.logout, name='logout'),
    path('profile/', view=views.profile, name='profile'),
    path('locale/', view=views.locale, name='locale'),
    #
    path('modules/', include('src.apps.help.modules.urls', namespace='modules')),
]
