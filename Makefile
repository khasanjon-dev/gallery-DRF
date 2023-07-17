make:
	python3 manage.py makemigrations
mig:
	python3 manage.py migrate
del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
admin:
	python3 manage.py createsuperuser --username admin #--phone_number 998337377060

reindex:
	python manage.py search_index --rebuild