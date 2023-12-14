import requests
import sentry_sdk
from celery import shared_task

from alone_celery_worker import app


@shared_task()
def check_route():
    c_error = None
    try:
        res = requests.get('http://django:8000/send/', timeout=4)
        if res.status_code != 200:
            raise requests.exceptions.RequestException("Can't reach the site")
    except requests.exceptions.RequestException as e:
        sentry_sdk.capture_exception(c_error)
        return False
    return True
