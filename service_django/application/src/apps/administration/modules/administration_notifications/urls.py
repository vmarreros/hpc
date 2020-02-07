from django.urls import path, include

app_name = 'administration'

urlpatterns = [
    path('alerts/', include(('src.apps.administration.modules.administration_notifications.alerts.urls', app_name), namespace='alerts')),
]
