# chat/routing.py
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
        # websocket connections of form ws/chat/roomname/ have
        # consumer ChatConsumer we defined attached to them
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
        #some cool regex i didnt write
]
