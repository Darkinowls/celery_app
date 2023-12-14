from celery import chain

from celery_app.celery_config import app


@app.task(queue='tasks')
def task_add(x, y):
    return x + y


@app.task(queue='tasks')
def task_multiply(num, multiplier):
    if multiplier == 0:
        raise ValueError('Can not multiply by 0')
    return num * multiplier


def do_chain():
    task_chain = chain(task_add.s(1, 2), task_multiply.s(3),
                       task_multiply.s(0), task_multiply.s(3))
    result = task_chain()
    print(result.get(propagate=False))
