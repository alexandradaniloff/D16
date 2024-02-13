
import os
from pathlib import Path
import allauth

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tc)26w*4e6)cj)y783z#i_du^p%n2h0eq^l%#12a7pbc!2+&(h'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['127.0.0.1']

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

# подтверждение регистрации по почте
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# подтверждение регистрации через консоль
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

ADMINS = (
    ('admin', 'alexandradaniloff@mail.ru'),
)
EMAIL_HOST = 'smtp.mail.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 2525  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'alexandradaniloff'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = '1CETJHvfMVRcQiqFLnDZ'  # пароль от почты
EMAIL_USE_SSL = False  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'alexandradaniloff@mail.ru'
EMAIL_ADMIN = 'alexandradaniloff@mail.ru'
SERVER_EMAIL = 'alexandradaniloff@mail.ru'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news.apps.NewsConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',

    'sign',
    'protect',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',


    'django_apscheduler',
]

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


SITE_ID = 2
SITE_URL = 'http://127.0.0.1:8000/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project.urls'




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates',)],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


DEBUG = False
#DEBUG = True
import logging

logger = logging.getLogger('django')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console_debug': {
             'level': 'DEBUG',
             'class': 'logging.StreamHandler',
             'formatter': 'formatter_debug',
             'filters': ['require_debug_true'],

        },
        'general_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'formatter_info',
            'filters': ['require_debug_false'],
        },

        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_warning',
            'filters': ['require_debug_true'],
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_error',
            'filters': ['require_debug_true'],
        },

        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'formatter_error',

        },
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'formatter_info',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
            'formatter': 'formatter_warning',
            'filters': ['require_debug_false'],
        },
    },

    'formatters': {
        'formatter_debug': {
            'format': '{levelname}  {asctime}   {message} \n',
            'style': '{',
        },
        'formatter_warning': {
            'format': '{levelname}  {asctime}  {message}  {pathname}\n',
            'style': '{',
        },
        'formatter_error': {
            'format': '{levelname} {asctime}  {message}  {pathname}  {exc_info}\n',
            'style': '{',
        },
        'formatter_info': {
            'format': '{levelname}  {asctime}  {module}  {message}\n',
            'style': '{',
        },

    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'loggers': {
         'django': {
              'handlers': ['console_debug', 'console_warning', 'console_error', 'general_file'],
              'level': 'DEBUG',
              'propagate': True,
         },
         'django.request': {
             'handlers': ['error_file', 'mail_admins'],
             'level': 'ERROR',
             'propagate': False,
         },
         'django.server': {
             'handlers': ['error_file', 'mail_admins'],
             'level': 'ERROR',
             'propagate': False,
         },
         'django.template': {
             'handlers': ['error_file'],
             'level': 'ERROR',
             'propagate': False,
         },
         'django.db.backends': {
              'handlers': ['error_file'],
              'level': 'ERROR',
              'propagate': False,
         },
         'django.security': {
             'handlers': ['security_file'],
             'level': 'WARNING',
             'propagate': False,
         }
    }
}