# Use the official MariaDB image as a parent image
FROM mariadb:latest

# Install Python3 and Pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the scripts directory contents into the container at /usr/src/app
COPY initial_migrations/ /usr/src/app/

# Copy the custom entrypoint script into the container and make it executable
COPY migrations_entrypoint.sh /usr/local/bin/
RUN apt-get update && \
    apt-get install -y mariadb-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    chmod +x /usr/local/bin/migrations_entrypoint.sh

# Run your custom entrypoint script
ENTRYPOINT ["migrations_entrypoint.sh"]
CMD ["mysqld"]
