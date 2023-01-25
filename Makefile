name := fastapi-bp
tag := dev
pwd := $(shell pwd)

run:
	@gunicorn app.main:app --config=src/gunicorn.conf.py --bind 0.0.0.0:5000 -k uvicorn.workers.UvicornWorker --chdir ${pwd}/src

build-base:
	@DOCKER_BUILDKIT=1 docker build . -t ${name}:base -f Dockerfile.base

build:
	@DOCKER_BUILDKIT=1 docker build . -t ${name}:dev -f Dockerfile --build-arg MYAPP_API_VERSION=${name}:dev

up:
	@docker-compose -f docker-compose.yml up -d

down:
	@docker-compose -f docker-compose.yml down

logs:
	@docker-compose logs -f api

clean:
	@find . -name "__pycache__" -prune -exec rm -rf {} \;

.PHONY: run build-base build up down logs clean