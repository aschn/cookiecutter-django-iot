# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

# Set up your local development environment
## Environment
You'll always need this:
```
export SECRET_KEY=[your value]
```

The default database is sqlite3. If you're using Postgres, then set up a database:
```
createdb {{ cookiecutter.repo_name }}
export DATABASE_URL=postgres://localhost/{{ cookiecutter.repo_name }}
```

This project is compatible with celery using a RabbitMQ (amqp) backend.
To use celery locally, [install RabbitMQ](https://www.rabbitmq.com/download.html),
then run rabbit in the background:
```
rabbitmq-server &
```

## Django
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

## Run the development server
```
python manage.py runserver
```

If you navigate to http://localhost:8000, you should see a filler template.

If you navigate to http://localhost:8000/admin, you should be able to sign in using your superuser account
and see admin pages for the `Device`, `Attribute`, and `PowerStatus` models.

# Make your app
Start by running the tests:
```
python manage.py test
```

The tests in the `devices` and `observations` apps should pass, but the tests in the `interactions` app should fail.

To make a working app, edit `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tasks.py`
to actually perform your tasks,
and update the tests at `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tests/test_tasks.py`.

If you add any kwargs to tasks, make sure to add them using `add_arguments` in `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/management/commands/interact.py`.

If you're using celery, you may also want to adjust the schedule of tasks in `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/schedule.py`.

And if you want a web UI that's more fun than the default admin, you'll want to add views to one or more of the apps (and to `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/urls.py`).

# Deploy to Heroku
## Basic deploy
After you've git-committed all your local changes, just create a Heroku app with the basic environment variables, push, and set up the initial database:
```
heroku create {{ cookiecutter.heroku_name }}
heroku config:set DJANGO_SETTINGS_MODULE={{ cookiecutter.repo_name }}.settings.production
heroku config:set SECRET_KEY=[your value]
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## Using management commands + Heroku Scheduler
Add the free Heroku Scheduler add-on:
```
heroku addons:create scheduler:standard
```
Then go to https://scheduler.heroku.com/dashboard and schedule management commands (eg `python manage.py interact refresh_all`).


## Using celery + CloudAMQP
Add the CloudAMQP add-on at the free level:
```
heroku addons:create cloudamqp:lemur
```
Then go to https://dashboard.heroku.com/apps/{{ cookiecutter.heroku_name }} and spin up one `scheduler` dyno.
