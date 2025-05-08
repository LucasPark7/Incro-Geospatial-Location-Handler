FROM python:alpine-slim

# env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libqp-dev \
    && rm -rf /var/liv/apt/lists/*

# python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# application code
COPY app/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]