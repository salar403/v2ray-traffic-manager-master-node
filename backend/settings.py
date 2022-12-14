from pathlib import Path
from backend.environments import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DEFAULT,
    REDIS_CACHE_LOCK,
    REDIS_TRAFFIC,
    REDIS_CELERY_BACKEND,
    REDIS_CELERY_BROKER,
    SWAGGER_URL,
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-@+3x_)p+mox=o_ne0a)-0+tkdwzr%l5o8dmek0j$)v4ffsk%hs"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "user",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DEFAULT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
    "traffic": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_TRAFFIC}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
    "cache_lock": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_LOCK}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

SWAGGER_SETTINGS = {"USE_SESSION_AUTH": False, "DEFAULT_API_URL": SWAGGER_URL}


CELERY_BROKER_URL = (
    f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BROKER}"
)
CELERY_RESULT_BACKEND = (
    f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_BACKEND}"
)
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 31540000}
CELERY_CREATE_MISSING_QUEUES = True


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
