from celery import shared_task


@shared_task
def task1():
    return "Hello World1"


@shared_task
def task2():
    return "Hello World2"
