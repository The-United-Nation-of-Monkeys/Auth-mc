#!/bin/bash

sleep 10

celery --app=src.config:celery_client worker -l INFO &

echo start

wait
