from celery import Celery
import sentry_sdk
import os
from datetime import timedelta
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_LINK"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
app = Celery('tasks')
app.config_from_object('celeryconfig')
app.conf.imports = ('newapp.tasks')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'task1': {
        'task': 'newapp.tasks.check_route',
        'schedule': timedelta(seconds=10),
    },

}
