import os
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'ubuntu',
        'PASSWORD': '1234',
<<<<<<< HEAD
        #'HOST': '172.31.23.193',
        #'PORT': '8000',
=======
        #'HOST': '',
        #'PORT': '',
>>>>>>> origin/master
    },
}
ALLOW_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
