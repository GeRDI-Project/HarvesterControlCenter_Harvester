"""
Django settings for hcc_py project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.contrib.messages import constants as message_constants

__author__ = "Jan Frömberg"
__copyright__ = "Copyright 2018, GeRDI Project"
__credits__ = ["Jan Frömberg"]
__license__ = "Apache 2.0"
__version__ = "3.9.0"
__maintainer__ = "Jan Frömberg"
__email__ = "jan.froemberg@tu-dresden.de"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '1efkn42-jh%e=r7%+owr*7s1hl06^tqalaf++p8sunex^(x^lj')

# SECURITY WARNING: don't run with debug turned on in production!
# There is a BUG?! If it will be settet via ENV Var, this is parsed as a string
DEBUG = os.environ.get('DEBUG', False) == 'True'
TEMPLATE_DEBUG = DEBUG

# A list/array of IPs and FQDNs
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
CSRF_TRUSTED_ORIGINS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Logging configuration
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            'stream': 'ext://sys.stdout',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'filedebug': {
            'class': 'logging.handlers.RotatingFileHandler',
            #'filters': ['require_debug_true'],
            'filename': './log/debug.log',
            'maxBytes': 1024*1024*2, #2MB
            'backupCount': 3,
            'formatter': 'simple',
        },
        'fileinfo': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './log/info.log',
            'maxBytes': 1024*1024*1, #1MB
            'backupCount': 3,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': LOGLEVEL,
        },
        'api': {
            'handlers': ['filedebug'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Configure Django to run in subpath
# https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-FORCE_SCRIPT_NAME
FORCE_SCRIPT_NAME = os.environ.get('FORCE_SCRIPT_NAME', '')

# Setup support for proxy headers, e.g. True
USE_X_FORWARDED_HOST = os.environ.get('USE_X_FORWARDED_HOST', '')

# e.g. a tuple with ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_PROXY_SSL_HEADER = (os.environ.get('SECURE_PROXY_SSL_HEADER', ''), '')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
}
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'
LOGIN_REDIRECT_URL = 'hcc_gui'
LOGOUT_REDIRECT_URL = 'hcc_gui'

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert-dark',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: 'alert-warning',
    message_constants.ERROR: 'alert-danger',
}

MESSAGE_LEVEL = message_constants.INFO

ROOT_URLCONF = 'hcc_py.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hcc_py.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # this setting (adding a subpath for db) maybe causes a db creation failure
        # on systems which uses manage.py runserver/test
        'NAME': os.path.join(BASE_DIR, 'db/', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'de-ch'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '%s/static/' % FORCE_SCRIPT_NAME
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
