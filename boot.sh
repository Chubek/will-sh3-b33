#!/bin/sh
exec gunicorn -b :8000 --worker-class gevent --workers=6 --threads=3 --access-logfile - --timeout 900 --error-logfile - app:app