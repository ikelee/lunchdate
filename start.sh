#!/bin/bash
TIMEOUT=120

# Start Gunicorn processes
echo Starting Gunicorn.
echo $PORT
exec gunicorn lunchdate.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout $TIMEOUT
