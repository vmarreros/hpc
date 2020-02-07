from django.urls import path

from . import views

app_name = 'bigdata_module01'

urlpatterns = [
    path('', view=views.index, name='index'),
]
