from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list/', view=views.ls, name='list'),

    path('edit/', view=views.edit, name='edit'),
    path('rename/', view=views.rename, name='rename'),
    path('download/', view=views.download, name='download'),
    path('paste/', view=views.paste, name='paste'),
    path('execute/', view=views.execute, name='execute'),
    path('delete/', view=views.delete, name='delete'),

    path('go-to/', view=views.go_to, name='go-to'),
    path('create-folder/', view=views.create_folder, name='create-folder'),
    path('create-file/', view=views.create_file, name='create-file'),
    path('upload/', view=views.upload, name='upload'),

    path('error/', view=views.error, name='error'),
]
