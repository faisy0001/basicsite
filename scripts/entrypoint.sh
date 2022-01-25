python manage.py migrate --no-input
python manage.py migrate accounts --run-syncdb
python manage.py createsuperuser --username faisy35 --email faisy@example.com --no-input --verbosity 3
python manage.py runserver 0.0.0.0:8000
exec "$@"