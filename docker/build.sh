#!/bin/bash

python3 -m alembic upgrade head 

python3 -u docker/start.py

python3 -m pytest

cd src

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000