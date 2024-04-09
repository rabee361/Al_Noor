from __future__ import absolute_import, unicode_literals
from celery import shared_task
@shared_task
def generate():
    one = []
    for i in range(500000):
        one.append(i)
    return one