PKG_NAME := src
PYTHONPATH := $(shell pwd)

run_all:
	@echo "---- Running Application ----"
	/opt/venv/bin/gunicorn -c gunicorn_conf.py main:app



docker-build:
	@echo "---- Building Docker Image ----"
	@docker build -t astolfo .


docker-compose:
	@echo "---- Running Docker Compose ----"
	cd ..
	@docker-compose up -d --build
	@echo "You can find the application at http://localhost:8000/docs"