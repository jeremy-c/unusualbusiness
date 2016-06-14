"""
WSGI config for (Un)usual Business project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/home/django/s-unusualbusiness/unusualbusiness'
if path not in sys.path:
    sys.path.append(path)

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.production'
os.environ['DJANGO_SECRET_KEY'] = '5bk5k_7vo7_qaz!9v^)-)8phwb3n-9gpa!m3*vv_8-56tvfc%2'
os.environ['DJANGO_ALLOWED_HOSTS'] = '.unusualbusiness.nl'
os.environ['DJANGO_ADMIN_URL'] = 'http://staging.unusualbusiness.nl/admin/'
os.environ['DJANGO_MAILGUN_API_KEY'] = 'key-768571d1216ec4254003e8d685afdd55'
os.environ['DJANGO_MAILGUN_SERVER_NAME'] = 'postmaster@staging.unusualbusiness.nl'
os.environ['DJANGO_OPBEAT_ORGANIZATION_ID'] = 'd6b41a720bb943a8972d95272c9adcfa'
os.environ['DJANGO_OPBEAT_APP_ID'] = '2d4526f650'
os.environ['DJANGO_OPBEAT_SECRET_TOKEN'] = 'b39de19517c79991a9c3b336676e065a1f1d95ef'
os.environ['DATABASE_URL'] = 'postgres://django:dxZ8X9sbnB@127.0.0.1:5432/django'
os.environ['DJANGO_SECURE_SSL_REDIRECT'] = 'False'

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
