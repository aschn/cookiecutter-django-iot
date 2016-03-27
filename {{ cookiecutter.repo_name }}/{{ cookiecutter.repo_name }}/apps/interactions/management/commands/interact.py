from django.core.management.base import BaseCommand
from {{ cookiecutter.repo_name }}.apps.interactions import tasks


class Command(BaseCommand):
    help = 'Run an interaction task'

    def add_arguments(self, parser):
        # may need to add more args here
        parser.add_argument('task_name')
        parser.add_argument('--device_id', required=False, type=int)
        parser.add_argument('--is_on', required=False, type=bool)

    def handle(self, *args, **options):
        # get task
        task_fn = getattr(tasks, options['task_name'])

        # run task with args
        result = task_fn(**options)
        self.stdout.write('Ran %s with result %s' % (options['task_name'], result))
