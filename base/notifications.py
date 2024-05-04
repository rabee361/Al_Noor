from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from .models import UserNotification , CustomUser , Pilgrim


def send_task_notification(employee,title,content):
    if employee.user.get_notifications:
        devices = FCMDevice.objects.filter(user=employee.user.id)
        devices.send_message(
                message =Message(
                    notification=Notification(
                        title=title,
                        body=content
                    ),
                ),
            )
        user = CustomUser.objects.get(id=employee.user.id)
        UserNotification.objects.create(user=user,content=content,title=title)



def send_event_notification(users,title,content):
    pilgrims = Pilgrim.objects.values_list('user')
    users = CustomUser.objects.filter(user__in=pilgrims)
    



def send_password(user,title,content):
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

