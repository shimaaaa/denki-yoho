# builder -------------------------
FROM python:3.10-buster as builder
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# setup poetry
RUN pip install poetry
ADD poetry.lock /app
ADD pyproject.toml /app
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

# runner -------------------------
FROM python:3.10-slim-buster as runner
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /app

# WORKDIR /app
# ADD dj_app /app/dj_app
# ADD uwsgi.ini /app

RUN apt update \
    && apt install -y libpq5 libxml2 curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=builder /usr/local/bin/celery /usr/local/bin/celery
COPY --from=builder /app /app
