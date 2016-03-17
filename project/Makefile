unexport DJANGO_SETTINGS_MODULE

all: db develop coverage

setup-db:
	@echo db.sqlite3

clean:
	find . -name \*.pyc -delete
	find . -name \*__pycache__ -delete

populate:
	python manage.py loaddata --app=board initial.yaml

makemigrations:
	python manage.py makemigrations

migrate: makemigrations
	python manage.py migrate

db: setup-db migrate populate

install:
	pip install -U -r requirements/base.txt

develop:
	pip install -U -r requirements/development.txt

show_urls:
	python manage.py show_urls

serve: clean
	python manage.py runserver

test: clean
	py.test --ignore=venv/

coverage: clean
	py.test --ignore=venv/ --cov-report term-missing  --cov=.

lint:
	flake8 .

check: lint coverage
