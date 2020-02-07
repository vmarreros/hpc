from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('administration_security/', include(('src.apps.administration.modules.administration_security.urls', app_name), namespace='administration_security')),
    path('administration_software/', include(('src.apps.administration.modules.administration_software.urls', app_name), namespace='administration_software')),
    path('administration_help/', include(('src.apps.administration.modules.administration_help.urls', app_name), namespace='administration_help')),
    path('administration_notifications/', include(('src.apps.administration.modules.administration_notifications.urls', app_name), namespace='administration_notifications')),
]
