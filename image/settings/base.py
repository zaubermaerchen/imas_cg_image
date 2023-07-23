# -*- coding: utf-8 -*-
"""
Django settings for image project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nk*79je2f7p)(c-q&-)qy!(wh&@wms0%l4zey5*fkp$(lh__sp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'idol',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'image.urls'

WSGI_APPLICATION = 'image.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


DEFAULT_IMAGE_SIZE = 'm'

IMAGE_SETTINGS = {
    's': {
        'attribute': ('s', 's', 's', 's', 's', 's'),
        'width': 130,
        'height': 163,
    },
    'm': {
        'attribute': ('m', 'm', 'm', 'm', 'm', 'm'),
        'width': 220,
        'height': 275,
    },
    'm2': {
        'attribute': ('m2', 'm2', 'm2', 'm2', 'm2', 'm2'),
        'width': 375,
        'height': 469,
    },
    'l': {
        'attribute': ('l', 'l', 'l', 'l', 'l', 'l'),
        'width': 640,
        'height': 800,
    },
    'l2': {
        'attribute': ('l', 'l', 'l', 'l', 'l_noframe', 'l_noframe'),
        'width': 640,
        'height': 800,
    },
    'ls': {
        'attribute': ('ls', 'ls', 'ls', 'ls', 'ls', 'ls'),
        'width': 120,
        'height': 375,
    },
    'xs': {
        'attribute': ('xs', 'xs', 'xs', 'xs', 'xs', 'xs'),
        'width': 100,
        'height': 100,
    },
}

IMAGE_URL_FORMAT = 'https://zaubermaerchen.info/imas_cg/image/card/%s/%s.jpg'
MOBAGE_URL = 'http://sp.pf-img-a.mbga.jp/12008305'
IDOL_DATA_API_URL_FORMAT = 'https://zaubermaerchen.info/imas_cg/api/idol/%d'
IMAGE_REDIS_KEY_FORMAT = 'imas_cg:image:%s:%s'

CORS_ORIGIN_ALLOW_ALL = True
