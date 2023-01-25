#!/bin/sh
set -e

if [ "$1" = 'gunicorn' ]; then
    shift
    exec gunicorn app.main:app \
        --config=gunicorn.conf.py \
        "$@"
else
    exec "$@"
fi
