modified:   monblog/blog/templates/blog/base.html
 23 #       modified:   monblog/blog/templates/blog/post_detail.html
 24 #       new file:   monblog/blog/templates/blog/post_draft_list.html
 25 #       new file:   monblog/blog/templates/registration/login.html
 26 #       modified:   monblog/blog/urls.py
 27 #       modified:   monblog/blog/views.py
 28 #       modified:   monblog/monblog/settings.py
 29 #       modified:   monblog/monblog/urls.pymodified:   monblog/blog/templates/blog/base.html
 23 #       modified:   monblog/blog/templates/blog/post_detail.html
 24 #       new file:   monblog/blog/templates/blog/post_draft_list.html
 25 #       new file:   monblog/blog/templates/registration/login.html
 26 #       modified:   monblog/blog/urls.py
 27 #       modified:   monblog/blog/views.py
 28 #       modified:   monblog/monblog/settings.py
 29 #       modified:   monblog/monblog/urls.pymodified:   monblog/blog/templates/blog/base.html
 23 #       modified:   monblog/blog/templates/blog/post_detail.html
 24 #       new file:   monblog/blog/templates/blog/post_draft_list.html
 25 #       new file:   monblog/blog/templates/registration/login.html
 26 #       modified:   monblog/blog/urls.py
 27 #       modified:   monblog/blog/views.py
 28 #       modified:   monblog/monblog/settings.py
 29 #       modified:   monblog/monblog/urls.py"""
Django settings for monblog project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6@c0$*gw6_9!a&00e@=inbozi#hzu_z$f^d9)xm5@9z6)n*uxd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'rolandiznogoud.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
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

ROOT_URLCONF = 'monblog.urls'

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

WSGI_APPLICATION = 'monblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Indian/Reunion'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
<<<<<<< HEAD
=======

LOGIN_REDIRECT_URL = '/'
>>>>>>> df9cac445a26f59cf47170c04b6a557786518e07
