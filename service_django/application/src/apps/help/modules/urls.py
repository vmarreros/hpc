from django.urls import path, include

app_name = 'modules'

urlpatterns = [
    path('help_document/', include('src.apps.help.modules.help_document.urls', namespace='help_document')),
]
