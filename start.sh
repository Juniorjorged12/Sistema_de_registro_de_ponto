#!/usr/bin/env bash
set -e
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:${PORT:-8000} app.wsgi:application
