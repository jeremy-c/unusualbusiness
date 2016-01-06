from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3h*$7zs0&y1h*32cf(s$j1dnxx=&0qltoj3g!-i8z-%w1+ptgt'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ub',
#         'USER': 'vagrant',
#         'PASSWORD': 'vagrant',
#         'HOST': '',
#         'PORT': '5432',
#     }
# }
DATABASES['default']['ATOMIC_REQUESTS'] = True

try:
    from .local import *
except ImportError:
    pass
