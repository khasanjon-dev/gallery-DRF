make:
	python3 manage.py makemigrations
mig:
	python3 manage.py migrate
del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
admin:
	python3 manage.py createsuperuser --phone 998909009090

reindex:
	python manage.py search_index --rebuild

add_users:
	python3 manage.py loaddata user.yaml