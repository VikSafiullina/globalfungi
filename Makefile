db-initial-setup:
	chmod +x migrations_entrypoint.sh
	chmod +x initial_migrations/*.py
	docker-compose build
	docker-compose up -d
	docker-compose logs db

db-up:
	docker-compose up -d

db-down:
	docker-compose down

db-reset:
	docker-compose down -v

config:
	cp common/config.example.py common/config.py

update-requirements:
	pip-compile --upgrade --output-file requirements.txt requirements.in
	pip3 install -r requirements.txt