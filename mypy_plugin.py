import os

from mypy_django_plugin import main


def plugin(version):
    os.environ.setdefault("DJANGO_ALLOWED_HOSTS", "")
    os.environ.setdefault("DJANGO_DEBUG", "0")
    os.environ.setdefault("DJANGO_SECRET_KEY", "terriblekey")
    os.environ.setdefault("DATABASE_URL", "")
    return main.plugin(version)
