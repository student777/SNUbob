import os
from .settings import *

#DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'snubob',
        'USER': 'ubuntu',
        'PASSWORD': '1234',
	# 'HOST': ,
	# 'PORT': ,
    },
}
ALLOW_HOSTS = ['*']


STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
