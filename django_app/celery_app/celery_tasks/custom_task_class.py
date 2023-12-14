from celery import Task

from celery_app.celery_config import app


class CustomTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))


app.Task = CustomTask


@app.task(queue='tasks')
def task_try_except_with_custom():
    raise ConnectionError('ConnectionError')
