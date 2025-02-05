#!/bin/bash

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Run cron script in the background if it's not a blocking process
./cron.sh &

# Start Gunicorn
exec gunicorn --bind 0.0.0.0:8080 HNG.wsgi:application
