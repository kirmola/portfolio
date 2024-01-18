# build_files.sh
python3.9 -m pip install -r requirements.txt

# make migrations
python3.9 manage.py tailwind build

if [ $ENV = "prod" ]; then
    python3.9 manage.py migrate
    python3.9 manage.py tailwind build
    python3.9 manage.py collectstatic --noinput
    python3.9 manage.py createsuperuser --noinput

fi