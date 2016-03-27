# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

# Local set-up
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

## Test and develop
```
python manage.py test
```

The tests in the `devices` and `observations` apps should pass, but the tests in the `interactions` app should fail.

To make a working app, edit `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tasks.py`
to actually perform your tasks,
and update the tests at `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tests/test_tasks.py`.
