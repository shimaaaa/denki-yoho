# builder -------------------------
FROM python:3.10-buster as builder
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# setup poetry
RUN pip install poetry
ADD ../poetry.lock /app
ADD ../pyproject.toml /app
RUN ../poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

# runner -------------------------
FROM python:3.10-slim-buster as runner
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH /app

RUN apt update \
    && apt install -y libpq5 libxml2 curl make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY --from=builder /usr/local/bin/alembic /usr/local/bin/alembic
COPY . /app

EXPOSE 8000

WORKDIR /app/server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
