from celery_config import celery_app
import time

@celery_app.task
def add(x, y):
    time.sleep(30)
    return x + y