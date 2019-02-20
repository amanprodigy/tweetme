from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zny4%!lw9!u8&ujj9f7kmd6$l6fa-v^3e#-=xiw^ynqt8=*mk('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'tweetme',
    'USER': 'django',
    'PASSWORD': 'django',
    'HOST': 'localhost',
    'PORT': '5432'
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# will be used to serve the files
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static-serve")
