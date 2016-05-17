"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# dev or prod
ENV_TYPE = 'dev'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2hzoll&97e%vl@5w1qqvj0zsblsjs+6y_9(9yxkf)g+r4y(z%5'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'app.urls'

STATIC_URL = '/static/'

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ORIGIN_WHITELIST = (
    'angularadmin'
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

AUTH_USER_MODEL = 'users.AppUser'

# option for registration
SITE_ID = 1

if ENV_TYPE == 'dev':
    DEBUG = True

    INSTALLED_APPS += (
        'rest_framework_swagger',
    )

    SWAGGER_SETTINGS = {
        'exclude_namespaces': [],
        'api_version': '0.1',
        'api_path': '/',
        'enabled_methods': [
            'get',
            'post',
            'put',
            'patch',
            'delete'
        ],
        'api_key': '',
        'is_authenticated': False,
        'is_superuser': False,
        'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
        'permission_denied_handler': None,
        'resource_access_handler': None,
        'base_path':'127.0.0.1:8000/docs',
        'info': {
            'contact': '',
            'description': '',
            'license': '',
            'licenseUrl': '',
            'termsOfServiceUrl': '',
            'title': 'API',
        },
        'doc_expansion': 'none',
    }

    # for test speed up
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher'
    ]

try:
    from mail import *
except ImportError:
    pass

try:
    from local import *
except ImportError:
    pass