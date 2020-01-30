from django.urls import path

from . import websocket

websocket_urlpatterns = [
    path('webssh/', websocket.WebSSH),
]
