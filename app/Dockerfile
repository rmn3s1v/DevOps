FROM python:3.11.14

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser

COPY --chown=appuser:appuser __init__.py ./app/__init__.py
COPY --chown=appuser:appuser main.py ./app/main.py
COPY --chown=appuser:appuser crud ./app/crud
COPY --chown=appuser:appuser db ./app/db
COPY --chown=appuser:appuser models ./app/models
COPY --chown=appuser:appuser routing ./app/routing

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
