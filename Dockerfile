FROM python:3.9-slim-bullseye

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN apt update && apt install -y build-essential \
    && pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install \
    && pip uninstall poetry -y \
    && apt --purge -y autoremove build-essential

COPY . .

 
ENTRYPOINT ["python", "/app/run_api.py"]
