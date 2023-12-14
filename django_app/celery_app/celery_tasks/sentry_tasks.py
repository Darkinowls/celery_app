from celery_app.celery_config import app


@app.task(queue='tasks')
def task_test_sentry():
    try:
        raise ValueError('HELLO SENTRY')
    except ValueError:
        pass  # SENTRY IGNORE THIS EXCEPTION
