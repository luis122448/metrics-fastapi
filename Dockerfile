FROM python:3.11.4

LABEL maintainer="luis122448@gmail.com" \
      description="Dockerfile para una aplicación de metricas con FastAPI y SQLite3" \
      version="1.0" \
      architecture="amd64"

WORKDIR /opt

# For sqlite3
RUN apt-get update && \
    apt-get install -y sqlite3 && \
    apt-get clean

# For python app
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./app /opt/app/
COPY ./database /opt/database/
COPY ./database/query.sql /opt/database/query.sql

# Initialize the database
RUN sqlite3 /opt/database/metrics.db < /opt/database/query.sql

EXPOSE 8083

CMD [ "python", "app/server.py" ]