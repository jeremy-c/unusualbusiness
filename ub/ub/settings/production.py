from .base import *


DEBUG = False


DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ub',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '',
        'PORT': '5432',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

try:
    from .local import *
except ImportError:
    pass
