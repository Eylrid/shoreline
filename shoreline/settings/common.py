"""
Common django settings for shoreline project.
"""

import os
from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#directory for deployment specific files
DEPLOY_DIR = os.path.join(BASE_DIR, 'deploy')
if not os.path.exists(DEPLOY_DIR):
    os.mkdir(DEPLOY_DIR)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shoreline.urls'

WSGI_APPLICATION = 'shoreline.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

#secret key, try to load from file
#or create a new one if the file doesn't exist

SECRET_FILE = os.path.join(BASE_DIR, 'deploy', 'SECRET')

if os.path.exists(SECRET_FILE):
    with open(SECRET_FILE, 'r') as file:
        SECRET_KEY = file.read().strip()
else:
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)
    with open(SECRET_FILE, 'w') as file:
        file.write(SECRET_KEY)
