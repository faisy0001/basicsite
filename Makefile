up:
	docker-compose up --remove-orphans
up-d:
	docker-compose up -d --remove-orphans
stop:
	docker-compose stop
down:
	docker-compose down
logs:
	docker-compose logs
shell:
	docker-compose exec web /bin/bash -c "python manage.py shell_plus"
migration:
		docker-compose exec web /bin/bash -c "sudo python manage.py makemigrations"
migrate:
		docker exec -it web /bin/bash python manage.py migrate
super_user:
		docker-compose exec web /bin/bash -c "sudo python manage.py createsuperuser --noinput "



