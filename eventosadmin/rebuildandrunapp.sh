#!/usr/bin/env bash
PORTA=8083
docker build --no-cache -t django -f Dockerfile .

docker rm -f auladefabricio-django || true
docker run -d --name auladefabricio-django -p ${PORTA}:80 django:latest
