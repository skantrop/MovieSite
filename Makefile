migrates:
	python manage.py makemigrations
	python manage.py migrate
run:
	python manage.py runserver
test:
	python manage.py test

run celery:
	celery -A movies worker --loglevel=info

