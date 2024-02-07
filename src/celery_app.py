import os
import time

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': 'posts.tasks.repeat_send_mail',
        'schedule': crontab()
    },
}

@app.task()
def debug_task():
    time.sleep(20)
    print('Hello from debug_task')
