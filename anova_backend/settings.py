"""
Django settings for anova_backend project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import environ
import os
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig',
    "bids.apps.BidsConfig",
    # 'drf_yasg',
    'drf_spectacular',
    "corsheaders",
    "rest_framework",  # Django REST Framework
    "rest_framework.authtoken",  # Django REST Framework Token Authentication
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'anova_backend.urls'

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

WSGI_APPLICATION = 'anova_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.NewUser"

############## MAKIING EMAIL REQUIRED ################
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# DATABASE URL
DATABASE_URL = env("DATABASE_URL")
import dj_database_url
if not DEBUG:
    db_from_env = dj_database_url.config(
        # default=DATABASE_URL,
        conn_max_age=500
    )
    DATABASES["default"].update(db_from_env)
    DATABASES["default"] = db_from_env

SITE_ID = 1

FRONTEND_URL = env('FRONTEND_URL')

##################### REST  FRAMEWORK #####################
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "anova_backend.authentication.CustomTokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

REST_AUTH = {
    "SESSION_LOGIN": False,
    "USER_DETAILS_SERIALIZER": "users.serializers.UserSerializer",
    # "TOKEN_SERIALIZER": "users.serializers.CustomTokenSerializer",
    

}

################### CORS HEADERS #####################
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
    "https://anova-api-426ae379974e.herokuapp.com",
    "https://anova-frontend.vercel.app",
]

# CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
    "https://anova-api-426ae379974e.herokuapp.com",
    "https://anova-frontend.vercel.app",
]

# ########### SWAGGER SETTINGS ################
# SWAGGER_SETTINGS = {
#     "SECURITY_DEFINITIONS": {
#         "basic": {"type": "basic"},
#         "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
#     },
#     # 'USE_SESSION_AUTH': False,
# }

SPECTACULAR_SETTINGS = {
    'TITLE': 'Anoda Project API',
    'DESCRIPTION': 'Anoda marketplace API for the Anoda Project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}