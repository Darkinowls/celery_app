import time

import celery.exceptions

from celery_app.celery_config import app


@app.task(queue='tasks', time_limit=5)
def task_add(x, y):
    time.sleep(4)
    return x + y


def do_with_timeout():
    result = task_add.delay(1, 2)
    try:
        print(result.get(propagate=False, timeout=2))
    except celery.exceptions.TimeoutError:
        print('TimeoutError')

    r2 = task_add.delay(4, 5)
    r2.revoke(terminate=True, signal='SIGKILL')
    print(r2.status)  # PENDING
    time.sleep(1)
    print(r2.status)  # REVOKED
