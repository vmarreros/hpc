from django.urls import path, include

app_name = 'notifications'

urlpatterns = [
    path('alerts/', include(('src.apps.notifications.modules.alerts.urls', app_name), namespace='alerts')),
]