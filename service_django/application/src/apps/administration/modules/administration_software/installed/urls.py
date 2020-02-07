from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list/', view=views.list, name='list'),
]
