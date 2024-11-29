from django.db import models
from django.db.models import Max



class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()


class GuideChats(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(chat_type='guide')\
                                    .annotate(latest_message_timestamp=Max('chatmessage__timestamp'))\
                                    .order_by('latest_message_timestamp')
    

class ManagerChats(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(chat_type='manager')\
                                    .annotate(latest_message_timestamp=Max('chatmessage__timestamp'))\
                                    .order_by('latest_message_timestamp')
    

