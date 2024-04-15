from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"al-noor/ws/chat/(?P<id>\d+)/(?P<id2>\d+)$", consumers.CreateMessage.as_asgi()),
]
