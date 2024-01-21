#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py tailwind build
python manage.py collectstatic --noinput
# python manage.py migrate