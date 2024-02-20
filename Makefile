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


prepare-env:
	@echo "Preparing environment..."
	@python3 -m venv venv
	@echo "Activating virtual environment and installing dependencies..."
	@pip install --upgrade pip
	@. venv/bin/activate && pip install --upgrade pip && pip install pip-tools && pip-compile requirements.in && pip install -r requirements.txt && pip install --upgrade graphene-sqlalchemy==3.0.0rc1 graphene==v3.3.0 && pip install "strawberry-graphql[debug-server]"
	@echo "Done!"

update-dependencies:
	@echo "Updating dependencies..."
	@python3 -m pip install --upgrade pip && pip-compile requirements.in && pip install -r requirements.txt
	@echo "Done!"