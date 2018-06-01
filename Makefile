db:
	mysql -uroot -ptoor -Dlog_db

        # create database log_db character set utf8;
        # show databases;

setup:
	python manage.py migrate
	python manage.py makemigrations
	python manage.py migrate --run-syncdb

run:
	sudo python manage.py runserver 0.0.0.0:80


run-dev:
	python manage.py runserver

