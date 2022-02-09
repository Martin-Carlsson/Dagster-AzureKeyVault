FROM python:3.10

RUN mkdir -p /opt/dagster/dagster_home

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

COPY dagster.yaml /opt/dagster/dagster_home/

RUN pip install --no-cache-dir --upgrade pip