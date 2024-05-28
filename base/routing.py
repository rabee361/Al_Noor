from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"al-noor/ws/manager-chat/(?P<chat_id>\d+)/(?P<user_id>\d+)$", consumers.CreateEmployeeMessage.as_asgi()),
    # re_path(r"al-noor/ws/employee-chat/(?P<chat_id>\d+)/(?P<user_id>\d+)$", consumers.CreateEmployeeMessage.as_asgi()),
    re_path(r"al-noor/ws/guide-chat/(?P<chat_id>\d+)/(?P<user_id>\d+)$", consumers.CreateGuideMessage.as_asgi()),
]
