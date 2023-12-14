from celery_app.celery_config import app


# BEATS ON in docker-compose.yml
@app.task(queue='tasks')
def task_b1(x, y, *, message):
    print(x, y)
    print(message)


@app.task(queue='tasks')
def task_b2():
    print("task_b2")
