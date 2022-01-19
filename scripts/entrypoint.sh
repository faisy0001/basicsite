python manage.py migrate --run-syncdb
python manage.py createsuperuser --username admin --email admin@example.com --no-input --verbosity 3
exec "$@"