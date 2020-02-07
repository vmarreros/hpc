from django.urls import path

from . import views

urlpatterns = [
    path('nodes/', view=views.nodes, name='nodes'),
    path('nodes_json/', view=views.nodes_json, name='nodes_json'),
    path('jobs/', view=views.jobs, name='jobs'),
    path('users/', view=views.users, name='users'),
]
