install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run python manage.py test

runserver:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes