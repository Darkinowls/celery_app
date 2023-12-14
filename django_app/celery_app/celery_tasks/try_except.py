from celery_app.celery_config import app


@app.task(queue='tasks')
def task_try_except():
    try:
        raise ConnectionError('ConnectionError')
    except ConnectionError as e:
        raise e
    except Exception as e:
        notify_admin()
        raise e


def notify_admin():
    pass
