#!bin/bash
pip3 install -r requirements.txt
python manage.py create_db
python manage.py makemigrations
python manage.py migrate
python manage.py fill_tr_tables --force_recreate FALSE
python manage.py fill_pve_pigeons --force_recreate FALSE
python manage.py runserver 0.0.0.0:8000