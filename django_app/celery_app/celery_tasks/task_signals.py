from celery.signals import task_failure

from celery_app.celery_config import app


# EVENTS ON in docker-compose.yml

@app.task(queue='tasks')
def task_raise_error():
    raise ValueError('SOME ERROR')


@task_failure.connect(sender=task_raise_error)
def handle_task_failure(sender, task_id, **kwargs):
    task_cleanup.delay(task_id)


@app.task(queue='tasks')
def task_cleanup(task_id, *args, **kwargs):
    print('CLEANUP')


def run_tasks():
    task_raise_error.delay()
