# {{ cookiecutter.project_name }}
{{ cookiecutter.description }}

# Local set-up
## Environment
```
createdb mydbname
export DATABASE_URL=postgres://localhost/mydbname
export SECRET_KEY=[your value]
```

## Django
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Test
```
python manage.py test
```

The tests in the `devices` and `observations` apps should pass, but the tests in the `interactions` app should fail.
To make a working app, edit `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tasks.py`
to actually perform your tasks,
and update the tests at `{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}/apps/interactions/tests/test_tasks.py`.
