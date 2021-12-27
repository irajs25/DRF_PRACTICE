from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backends.settings')

app = Celery('backends')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# celery beat settings
# In alternate here we can use apply_async()
hr = '18'
mt = '22'
app.conf.beat_schedule = {
    'send-mail-everyday-at-8': {
        'task': 'email_send_app.tasks.send_mail_func',
        'schedule': crontab(hour=hr, minute=mt),
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))