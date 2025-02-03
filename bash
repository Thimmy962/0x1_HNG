#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
gunicorn --bind 0.0.0.0:8080 HNG.wsgi:application
