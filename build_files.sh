# build_files.sh
pip install -r requirements.txt
which npm

if [ $ENV = "prod" ]; then

    echo "Now Running on PRODUCTION environment"
    python3.9 manage.py migrate
    python3.9 manage.py collectstatic --noinput
    python3.9 manage.py createsuperuser --noinput

elif [ $ENV = "dev" ]; then

    echo "Now Running on DEVELOPMENT environment"

    python3.9 manage.py collectstatic --noinput

fi