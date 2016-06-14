Thank you for using DigitalOcean's Django Application.
We have created a default Django application that can be seen from http://46.101.214.119/

You can use the following SFTP credentials to upload your files (using FileZilla/WinSCP/Rsync):
Host: 46.101.214.119
User: django
Pass: qiTiREMVuM

You can use the following Postgres database credentials:
DB: django
User: django
Pass: dxZ8X9sbnB

Nginx listens on public IP (46.101.214.119) port 80 and forwards requests to Gunicorn on port 9000
Nginx access log is in /var/log/nginx/access.log and error log is in /var/log/nginx/error.log
Gunicorn is started using an Upstart script located at /etc/init/gunicorn.conf
To restart your Django project, run : sudo service gunicorn restart

You can find more information on using this image at: http://do.co/djangoapp
-------------------------------------------------------------------------------------
To delete this message of the day: rm -rf /etc/motd.tail

user: linksmith
pw: 94LehyzHS7dHYvfe


#!/bin/bash
# This hook is sourced after this virtualenv is activated.

export DJANGO_SETTINGS_MODULE='config.settings.production'
export DJANGO_SECRET_KEY='5bk5k_7vo7_qaz!9v^)-)8phwb3n-9gpa!m3*vv_8-56tvfc%2'
export DJANGO_ALLOWED_HOSTS='.unusualbusiness.nl'
export DJANGO_ADMIN_URL='http://staging.unusualbusiness.nl/admin/'
export DJANGO_MAILGUN_API_KEY='key-768571d1216ec4254003e8d685afdd55'
export DJANGO_MAILGUN_SERVER_NAME='postmaster@staging.unusualbusiness.nl'

export DJANGO_OPBEAT_ORGANIZATION_ID='d6b41a720bb943a8972d95272c9adcfa'
export DJANGO_OPBEAT_APP_ID='2d4526f650'
export DJANGO_OPBEAT_SECRET_TOKEN='b39de19517c79991a9c3b336676e065a1f1d95ef'

export DATABASE_URL='postgres://django:dxZ8X9sbnB@127.0.0.1:5432/django'


source $VIRTUAL_ENV/bin/postactivate
& python manage.py migrate --fake-initial

http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-pythonanywhere.html
