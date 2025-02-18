import os
from pathlib import Path
from urllib.parse import urlparse

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Load envvars from .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# False by default, change it in .env
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Must have a valid value if DEBUG is False
HOST_URL = os.getenv("HOST_URL")  # eg "https://www.google.com"
if HOST_URL:
    ALLOWED_HOSTS = [urlparse(HOST_URL).netloc]  # if using above example, will resolve to www.google.com
    CSRF_TRUSTED_ORIGINS = [HOST_URL]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    CORS_ALLOWED_ORIGINS = [
        "https://storage.googleapis.com",
        HOST_URL,
    ]
else:
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # For SwaggerUI
    "drf_spectacular",
    # "drf_yasg",
    # Django extensions
    "corsheaders",
    "rest_framework",
    # Custom apps
    "ecommerce.store",
]
# DRF config:
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # From django-cors-headers
    "corsheaders.middleware.CorsMiddleware",
]

UI_BIND_PORT = os.getenv("UI_BIND_PORT", 3000)
CORS_ORIGIN_WHITELIST = [
    f"http://localhost:{UI_BIND_PORT}",  # The default port for create-react-app
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "sqlite3").lower()  # Supports 'sqlite3', 'postgres' and mysql

if DATABASE_ENGINE == "sqlite3":
    DATABASE_LOCATION = os.getenv("DB_LOCATION", "db.sqlite3")  # Always relative to project dir
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / DATABASE_LOCATION,
        }
    }

elif DATABASE_ENGINE == "postgres":
    DB_SERVER = os.getenv("DB_SERVER", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "postdb")
    DB_USER = os.getenv("DB_USERNAME", "admin")
    DB_PASS = os.getenv("DB_PASSWORD", "1q2w3e4r")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": DB_SERVER,
            "PORT": DB_PORT,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASS,
        }
    }

elif DATABASE_ENGINE == "mysql":
    DB_SERVER = os.getenv("DB_SERVER", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "mysqldb")
    DB_USER = os.getenv("DB_USERNAME", "admin")
    DB_PASS = os.getenv("DB_PASSWORD", "1q2w3e4r")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": DB_SERVER,
            "PORT": DB_PORT,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASS,
        }
    }

else:
    raise ImproperlyConfigured("Unknown database engine '{!s}'".format(DATABASE_ENGINE))


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SwaggerUI settings
SPECTACULAR_SETTINGS = {
    "TITLE": "DRF Ecommerce API",
    "DESCRIPTION": "This is a django backend API service runnning DRF",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
