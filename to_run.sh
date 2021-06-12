#!/bin/sh

#run application using gunicorn
eval gunicorn -w 4 -b 0.0.0.0:8000 --log-file gunicorn.log --log-level DEBUG --reload app:app
