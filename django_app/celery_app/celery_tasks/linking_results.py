import sys
import time

from celery_app.celery_config import app


@app.task(queue='tasks')
def task_long_time(x):
    time.sleep(1)
    return x + 1


@app.task(queue='tasks')
def task_process_result(result):
    sys.stdout.write('process_result: {0}\n'.format(result))
    sys.stdout.flush()
    result = result - 100
    return result


########################
@app.task(queue='tasks')
def task_error(x):
    raise ValueError('THAT IS ERROR')


@app.task(queue='tasks')
def task_process_error(request, exc, traceback):
    sys.stdout.write('process_error: {0}\n'.format(exc.__str__()))
    sys.stdout.flush()
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")  # inside celery worker
    print('process_error: {0}\n'.format(exc.__str__()))
    return "ERROR"


def run_task():
    result = task_long_time.apply_async((1,), link=[task_process_result.s()])
    print(result.get())  # 2

    task_error.apply_async((1,), link_error=[task_process_error.s()])
