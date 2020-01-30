from django.urls import path

from . import views

app_name = 'terminal'

urlpatterns = [
    path('', view=views.init, name='init'),
]
