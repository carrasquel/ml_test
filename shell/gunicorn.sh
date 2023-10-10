#!/bin/sh

mkdir -p /var/log/gunicorn
touch /var/log/gunicorn/gunicorn-error.log

gunicorn --chdir app wsgi:app -w 2 --threads 2 --error-logfile /var/log/gunicorn/gunicorn-error.log -b 0.0.0.0:80

exec "$@"