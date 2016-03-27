from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.repo_name }}.settings.dev')
app = Celery('{{ cookiecutter.repo_name }}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

# autodiscover tasks in any app
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# set schedule
from {{ cookiecutter.repo_name }}.apps.interactions.schedule import SCHEDULE
app.conf.CELERYBEAT_SCHEDULE = SCHEDULE
