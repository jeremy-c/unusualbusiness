web: gunicorn config.wsgi:application
worker: celery worker --app=unusualbusiness.taskapp --loglevel=info
