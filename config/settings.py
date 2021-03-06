"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&uii1=nb97-5y=oc%ob&es7%&a*%3up_6a%@c#8=8=(dg%6o-3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'crispy_forms',
    'whitenoise.runserver_nostatic',
    'widget_tweaks',
    'explorer',

    # locally developed apps
    'accounts',
    'pages',
    'pilot_currency',
    'pilot_log',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'accounts.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Constants for Models
MISSION_CHOICES = [
    ('LP', 'Leadplane'),
    ('SJ', 'Smokejumper'),
    ('PP', 'Pilot Proficiency'),
    ('AD', 'Administrative'),
    ('OT', 'Civilian/Military'),
    ('AA', 'Air Attack'),
    ('MT', 'Maintenance'),
    ('LOG', 'Logistics'),
    ('ASM', 'Aerial Supervision Module'),
    ('HC', 'Helicopter'),
    ('IR', 'Infrared'),
    ('RC', 'Recon'),
    ('PH', 'Photo'),
    ('BC', 'Back Country'),
]

AIRCRAFT_TYPES = [
    ('SD-3', 'Sherpa'),
    ('KA', 'King Air'),
    ('206', 'C-206')
]

TAIL_NUMBERS = [
    ('N162Z', 'N162Z'),
    ('N163Z', 'N163Z'),
    ('N174Z', 'N174Z'),
    ('N176Z', 'N176Z'),
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

LOGIN_REDIRECT_URL = '/pilot_currency'
LOGOUT_REDIRECT_URL = 'home'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Explorer settings for reports
EXPLORER_CONNECTIONS = { 'Default': 'default' }
EXPLORER_DEFAULT_CONNECTION = 'default'
EXPLORER_PERMISSION_VIEW = lambda r: r.user.is_supervisor

# Slick Reporting settings
def start_date():
    d = datetime.datetime.today()
    return datetime.datetime(d.year - 1, d.month, d.day, 0, 0)


# Django Debug Toolbar settings
INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}