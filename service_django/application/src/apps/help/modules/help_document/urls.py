from django.urls import path, re_path

from . import views

app_name = 'help_document'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list/', view=views.list, name='list'),
    re_path(r'^content/(?P<pk>\d+)/$', view=views.content, name='content'),
]
