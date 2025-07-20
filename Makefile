server:
	python manage.py runserver

migrations:
	python manage.py makemigrations 

migrate:
	python manage.py migrate

container:
	docker compose up -d

build:
	docker compose build --no-cache
