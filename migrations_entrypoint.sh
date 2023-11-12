#!/bin/bash
set -e

# Original docker-entrypoint for MariaDB to setup initial DB and user
docker-entrypoint.sh /usr/bin/mysqld &

# Wait for the database service to start up
echo "Waiting for MariaDB to start up..."
until /usr/bin/mysqladmin ping -h localhost -u root --password="$MARIADB_ROOT_PASSWORD" --silent; do
    sleep 1
done

echo "MariaDB started"

# Run Python scripts in the order
# Assuming scripts are located in /usr/src/app/ and are executable
for script in /usr/src/app/[0-9][0-9]_*.py; do
    echo "Executing $script"
    python3 "$script"
done

# Bring MariaDB back into the foreground for Docker's PID 1
fg %1
