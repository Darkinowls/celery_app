from celery import group

from celery_app.celery_config import app


@app.task(queue='tasks')
def task_job(x):
    try:
        if x == 2:
            raise ConnectionError('ConnectionError')
    except ConnectionError as e:
        handle_failure.apply_async((x, e.__str__()))
        raise  # optional
    return x


@app.task(queue='dead_letter')
def handle_failure(value, error: str = ''):
    print('ERROR: {0} {1}'.format(value, error))


def run_tasks():
    g = group(task_job.s(i) for i in range(5))
    g.apply_async()
