from celery import group
from celery.result import AsyncResult

from celery_app.celery_config import app


@app.task(queue='tasks')
def task_k(num):
    if num == 3:
        raise ValueError('num can not be 3')
    return num


def handle_result(result: AsyncResult):
    print(result.failed())
    if result.successful():
        print(f'SUCCESSFUL {result.get()}')
    elif result.status == 'REVOKED':
        print(f'REVOKE {result.id}')
    elif result.failed():
        print(f'FAIL {result.id}')


def run_tasks():
    g = group(task_k.s(i) for i in range(5))
    result = g.apply_async()
    result.get(
        # disable_sync_subtasks=False,
        propagate=False)
    for r in result:
        handle_result(r)
