from celery.schedules import crontab


SCHEDULE = {
    'refresh_all': {
        'task': '{{ cookiecutter.repo_name }}.apps.interactions.tasks.refresh_all',
        'schedule': crontab(minute='*/5')
    },

}
