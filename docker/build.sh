#!/bin/bash

python3 -m alembic upgrade head 

bash /docker/broker.sh

python3 -u /docker/start.py

gunicorn src.main:app --workers 4 --timeout 100 --worker-class uvicorn.workers.UvicornWorker --bind="0.0.0.0:8000" &

celery -A src.config:celery_client worker --loglevel=info &

# uvicorn main:app &

echo huesos

wait