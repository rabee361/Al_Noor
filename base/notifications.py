from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from .models import UserNotification


def send_task_notification(employee,title,content):
    if employee.user.get_notifications:
        devices = FCMDevice.objects.filter(user=employee.user.id)
        title = 'انشاء طلب'
        body = f'تم ارسال طلبك بنجاح'
        devices.send_message(
                message =Message(
                    notification=Notification(
                        title=title,
                        body=content
                    ),
                ),
            )
        UserNotification.objects.create(user=employee.user,content=content,title=title)



def send_event_notification(users,title,content):
    pass