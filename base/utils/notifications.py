from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification , UnregisteredError
from firebase_admin.exceptions import InvalidArgumentError
from ..models import UserNotification , CustomUser , Guide , Pilgrim , BaseNotification
from django.db.models import Q


def send_task_notification(employee,title,content):
    if employee.user.get_notifications:
        title = "لديك مهمة جديدة"
        devices = FCMDevice.objects.filter(user=employee.user.id)
        for device in devices:
            try:
                device.send_message(
                        message =Message(
                            notification=Notification(
                                title=title,

                            body=content
                        ),
                    ),
                )
            except UnregisteredError:
                pass
            except InvalidArgumentError:
                pass
        UserNotification.objects.create(user=employee.user,content=content,title=title)





def send_pilgrims_notification(title,content,sentBy):
    guide = Guide.objects.get(user=sentBy)
    pilgrims = Pilgrim.objects.filter(guide=guide).values('user')
    users = CustomUser.objects.filter((Q(user_type='حاج') & Q(get_notifications=True) )& Q(id__in = pilgrims))
    for user in users:
        devices = FCMDevice.objects.filter(user=user.id)
        for device in devices:
            try:
                device.send_message(
                    message =Message(
                        notification=Notification(
                        title=title,
                        body=content
                        ),
                    ),
                )
            except UnregisteredError:
                pass
            except InvalidArgumentError:
                pass
        UserNotification.objects.create(user=user,content=content,title=title)
    BaseNotification.objects.create(title=title,content=content,sentBy=sentBy)
    



def send_event_notification(title,content,sentBy):
    users = CustomUser.objects.filter(Q(user_type='حاج') & Q(get_notifications=True))
    for user in users:
        devices = FCMDevice.objects.filter(user=user.id)
        for device in devices:
            try:
                device.send_message(
                    message =Message(
                        notification=Notification(
                            title=title,
                            body=content
                        ),
                    ),
                )
            except UnregisteredError:
                pass
            except InvalidArgumentError:
                pass
        UserNotification.objects.create(user=user,content=content,title=title)
    BaseNotification.objects.create(title=title,content=content,sentBy=sentBy)



def send_code(user,title,content):
    if user.get_notifications:
        devices = FCMDevice.objects.filter(user=user.id)
        devices.send_message(
                message =Message(
                    notification=Notification(
                        title=title,
                        body=content
                    ),
                ),
            )
        UserNotification.objects.create(user=user,content=content,title=title)

