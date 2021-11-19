#!bin/bash
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py fill_tr_tables
python manage.py runserver 0.0.0.0:8000