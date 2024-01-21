#!/usr/bin/env bash
# exit on error
set -o errexit
which npm
poetry install

python manage.py tailwind build
python manage.py collectstatic --noinput
# python manage.py migrate