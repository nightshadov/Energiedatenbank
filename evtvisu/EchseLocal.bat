
python manage.py makemigrations
python manage.py migrate --run-syncdb

start "" http://127.0.0.1:8000

python manage.py runserver 127.0.0.1:8000

pause