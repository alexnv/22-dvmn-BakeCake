# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /opt/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /opt/app
RUN python manage.py migrate
RUN python manage.py loaddata demo-data --format JSON
CMD [ "python", "./manage.py", "runserver"]
