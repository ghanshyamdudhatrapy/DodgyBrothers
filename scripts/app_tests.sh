#!/usr/bin/env bash
docker-compose exec -T django python manage.py behave
