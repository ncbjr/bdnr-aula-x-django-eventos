#!/usr/bin/env bash
PORTA=8084
docker build --no-cache -t fastapi -f Dockerfile .

docker rm -f auladefabricio-fastapi || true
docker run -d  -v $PWD:/app --name auladefabricio-fastapi -p ${PORTA}:80 fastapi
