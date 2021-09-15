#!/bin/sh
exec gunicorn -b :8000 --access-logfile - --timeout 800 --error-logfile - app:app