#!/bin/sh
exec gunicorn -b :8000 --worker-class gevent --access-logfile - --timeout 900 --error-logfile - app:app