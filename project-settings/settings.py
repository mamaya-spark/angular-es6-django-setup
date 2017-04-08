"""
Using Django 1.10.5.
"""

import os

BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ENV       = os.environ['DJANGO_ENV']
SECRET_KEY       = os.environ['DJANGO_SECRET_KEY']
APP_IP           = os.environ['APP_IP']
APP_BACKEND_IP   = os.environ['APP_BACKEND_IP']
APP_PSQL_DB_NAME = os.environ['APP_PSQL_DB_NAME']
APP_PSQL_DB_HOST = os.environ['APP_PSQL_DB_HOST']
APP_PSQL_DB_USER = os.environ['APP_PSQL_DB_USER']
APP_PSQL_DB_PASS = os.environ['APP_PSQL_DB_PASS']
APP_PSQL_DB_PORT = os.environ['APP_PSQL_DB_PORT']

if DJANGO_ENV == 'production':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = [
    APP_IP,
    APP_BACKEND_IP
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': APP_PSQL_DB_NAME,
        'USER': APP_PSQL_DB_USER,
        'PASSWORD': APP_PSQL_DB_PASS,
        'HOST': APP_PSQL_DB_HOST,
        'PORT': APP_PSQL_DB_PORT
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
]

STATIC_URL = '/static/'
