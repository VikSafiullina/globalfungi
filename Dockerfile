FROM python:3.11.8-slim
WORKDIR /python-docker

# Install necessary system dependencies including curl
RUN apt-get update && apt-get install -y \
    gnupg \
    gcc \
    g++ \
    unixodbc-dev \
    curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && rm -rf /var/lib/apt/lists/*

RUN sh -c "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -" \
    && apt-get update \
    && sh -c "curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list" \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools18

COPY requirements.in requirements.in
RUN pip install pip-tools
RUN pip-compile requirements.in > requirements.txt
RUN sed -i '/pyobjc/d' requirements.txt
RUN pip install -r requirements.txt
RUN pip install 'strawberry-graphql[debug-server]'
COPY . .
RUN chmod 777 /python-docker/_run.sh
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
