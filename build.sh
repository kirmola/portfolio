#!/usr/bin/env bash
# exit on error
set -o errexit
poetry install

cd theme/static_src
npm install
npm run build
cd ../..
python manage.py collectstatic --noinput
# python manage.py migrate