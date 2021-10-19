"""
Django settings for django_chat_channels_redis project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import django_heroku
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uqs+(7fn)@%_jt^2d=xfr@6(!ttzcb=i^-q)cr9!wh@exo^6=c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django Channels
    'channels',

    # Django Form Customization
    "crispy_forms",
    'widget_tweaks',

    # Apps
    'chat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # When not running with the built-in development server, you'll need to either
    # use whitenoise which does this as a Django/WSGI middleware in order to load
    # Django static files using Uvicorn
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_chat_channels_redis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'django_chat_channels_redis.wsgi.application'
ASGI_APPLICATION = 'django_chat_channels_redis.asgi.application'

if DEBUG:
    CHANNEL_LAYERS = {
        'default': {
            # DO NOT USE IN PRODUCTION!
            # In-memory channel layers operate with each process as a separate layer.
            # This means that no cross-process messaging is possible.
            # As the core value of channel layers is to provide distributed messaging,
            # in-memory usage will result in sub-optimal performance,
            # and ultimately data-loss in a multi-instance environment.
            # 'BACKEND': 'channels.layers.InMemoryChannelLayer',

            # channels_redis is the only official Django-maintained channel layer supported for production use.
            # The layer uses Redis as its backing store, and supports both a single-server and sharded configurations,
            # as well as group support. To use this layer you’ll need to install the channels_redis package.
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            'CONFIG': {
                'hosts': [('127.0.0.1', 6379)],
            }
        }
    }
else:
    CHANNEL_LAYERS = {
        'default': {
            # DO NOT USE IN PRODUCTION!
            # In-memory channel layers operate with each process as a separate layer.
            # This means that no cross-process messaging is possible.
            # As the core value of channel layers is to provide distributed messaging,
            # in-memory usage will result in sub-optimal performance,
            # and ultimately data-loss in a multi-instance environment.
            # 'BACKEND': 'channels.layers.InMemoryChannelLayer',

            # channels_redis is the only official Django-maintained channel layer supported for production use.
            # The layer uses Redis as its backing store, and supports both a single-server and sharded configurations,
            # as well as group support. To use this layer you’ll need to install the channels_redis package.
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            'CONFIG': {
                "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
            }
        }
    }


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Heroku database configurations
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# django_heroku.settings(locals())
# options = DATABASES['default'].get('OPTIONS', {})
# options.pop('sslmode', None)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# When not running with the built-in development server, you'll need to either
# use whitenoise which does this as a Django/WSGI middleware in order to load
# Django static files using Uvicorn
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default Django Authentication Routes
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'