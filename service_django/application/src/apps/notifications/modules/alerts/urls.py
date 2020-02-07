from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^detail/(?P<pk>\d+)/$', view=views.detail, name='detail'),
    re_path(r'^unread/(?P<pk>\d+)/$', view=views.unread, name='unread'),
    re_path(r'^delete/(?P<pk>\d+)/$', view=views.delete, name='delete'),
]