from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('vars/', view=views.vars, name='vars'),
]