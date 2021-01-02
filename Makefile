runserver:
	poetry run python manage.py runserver

lint:
	poetry run flake8 task_manager

requirements:
	poetry export -f requirements.txt -o requirements.txt --without-hashes