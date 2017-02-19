from .settings import *

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'snubob',
                'USER': 'postgres',
                'PASSWORD': '1234',
                },
}
