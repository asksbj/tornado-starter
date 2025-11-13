# syntax=docker/dockerfile:1.7

FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_PORT=8888

WORKDIR /app

# Install minimal OS deps (optional: add build tools only if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application
COPY . .

# Expose application port
EXPOSE ${APP_PORT}

# Non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# If you pass a different port at runtime, ensure APP_PORT is set
CMD ["python", "-m", "tornado_starter"]


