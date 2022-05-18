#!/usr/bin/env bash
docker-compose exec -T django coverage report
docker-compose exec -T django coverage html
