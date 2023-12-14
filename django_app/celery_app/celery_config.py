import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_app.settings')

app = Celery('celery_app')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
    Queue(
        'dead_letter',
        # it has Exchange('dead_letter'),
        routing_key='dead_letter'),
]
app.conf.task_acks_late = True  # acknowledge after task is done
app.conf.task_reject_on_worker_lost = True  # reject task if worker is lost
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1  # 1 task per worker
app.conf.worker_concurrency = 1  # 1 worker per queue

# app.conf.beat_schedule = {
#     'task_b1': {
#         'task': 'celery_app.celery_tasks.task_scheduling.task_b1',
#         'schedule': timedelta(seconds=5),
#         'kwargs': {'message': 'Hello World FROM TASK B1'},
#         'args': (1, 2),
#         'options': {
#             'queue': 'tasks',
#             'priority': 10
#         }
#     },
#     'task_b2': {
#         'task': 'celery_app.celery_tasks.task_scheduling.task_b2',
#         'schedule': crontab(minute='*/1'),
#
#     }
# }


def discover_tasks():
    base_dir = os.getcwd()
    task_folder = os.path.join(base_dir, 'celery_app', 'celery_tasks')
    if not os.path.exists(task_folder) or not os.path.isdir(task_folder):
        return None

    task_modules = []
    for file in os.listdir(task_folder):
        if not file.startswith('__') and file.endswith('.py'):
            shorted_filename = file.split('.')[0]
            module_name = f"celery_app.celery_tasks.{shorted_filename}"
            module = __import__(module_name, fromlist=['*'])
            task_modules.extend([f"{module_name}.{name}"
                                 for name in dir(module)
                                 if name.startswith('task')])
    app.autodiscover_tasks(task_modules)


discover_tasks()
app.autodiscover_tasks()

# @app.task(queue='tasks')
# def t1(a,b, message=None):
#     result = a + b
#     return f"{message}:Hello World {result}"
#
#
# @app.task(queue='tasks')
# def t2(x):
#     time.sleep(3)
#     return "Hello World2"
#
#
# @app.task(queue='tasks')
# def t3(x):
#     time.sleep(3)
#     return "Hello World3"


# app.conf.task_default_rate_limit = '1/m' # 1 task per minute in a queue
# app.conf.task_routes = {
#     'newapp.tasks.task1': {'queue': 'queue1'},
#     'newapp.tasks.task2': {'queue': 'queue2'},
# }
# app.conf.broker_transport_options = {
#     # 'priority_steps': list(range(10)),
#     'separator': ':',
#     'queue_order_strategy': 'priority',
# }
