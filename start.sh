#!/bin/bash
TIMEOUT=120

# Start Gunicorn processes
echo Starting Gunicorn.
echo process.env.PORT
exec gunicorn lunchdate.wsgi:application \
    --bind process.env.PORT \
    --workers 3 \
    --timeout $TIMEOUT
