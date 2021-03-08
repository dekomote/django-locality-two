#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import django
from django.conf import settings
from django.test.runner import DiscoverRunner


sys.path.insert(0, abspath(dirname(__file__)))


DEFAULT_SETTINGS = dict(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        },
    },
    SECRET_KEY="not a secret",
    ALLOWED_HOSTS=["localhost"],
    ROOT_URLCONF="locality.urls",
    STATIC_URL="/static/",
    INSTALLED_APPS=[
        "django.contrib.messages",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.admin",
        "locality",
    ],
    MIDDLEWARE=[
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],
    TEMPLATES=[
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
    ],
    LOGGING={
        "version": 1,
        "disable_existing_loggers": True,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
)


def main():

    settings.configure(**DEFAULT_SETTINGS)
    django.setup()

    failures = DiscoverRunner(failfast=False).run_tests(["locality.tests"])
    sys.exit(failures)


if __name__ == "__main__":
    main()
