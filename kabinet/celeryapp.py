import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kabinet.settings')

from django.conf import settings

app = Celery('kabinet', broker=settings.BROKER)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(name='load_calls_from_uiscom')
def load_calls_from_uiscom():
    from apps.calls.services import load_calls_from_uiscom
    load_calls_from_uiscom()
