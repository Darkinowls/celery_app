import time

from celery import shared_task


# celery - highest priority

from django.core.management import call_command

@shared_task(queue='tasks')
def managment_command():
    call_command('do_command')

#
# @shared_task(task_rate_limit='1/m')
# def tp1(queue='celery:1'):
#     return "Hello World1"
#
#
# @shared_task()
# def tp2(queue='celery:2'):
#     time.sleep(3)
#     return "Hello World2"
#
#
# @shared_task()
# def tp3(queue='celery:3'):
#     time.sleep(3)
#     return "Hello World3"
