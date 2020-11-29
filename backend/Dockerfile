 FROM python:3
 ADD requirements.txt .
 RUN pip install -r requirements.txt
 RUN python manage.py makemigrations
 RUN python manage.py migrate
 EXPOSE 8000
