from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DATABASE-NAME', 'django_shop'),
#         'USER': os.environ.get('DATABASE-USER', 'django_shop'),
#         'PASSWORD': os.environ.get('DATABASE-PASSWORD', 'django_shop.123456'),
#         'HOST': os.environ.get('DATABASE-HOST', 'database'),
#         'PORT': os.environ.get('DATABASE-PORT', 5432)
#     }}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "sqlite3",
    }
}