runserver:
	poetry run python manage.py runserver

lint:
	poetry run flake8

requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes