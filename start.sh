#!/bin/bash
TIMEOUT=120

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn lunchdate.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --timeout $TIMEOUT
