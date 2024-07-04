from celery import Celery
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

celery_app = Celery(
    'worker',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['tasks']
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],  
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    worker_concurrency=1
)
