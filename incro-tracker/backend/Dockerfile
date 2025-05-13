FROM python:3.10-alpine

WORKDIR /app

# system dependencies
RUN apk update && apk add --no-cache gcc musl-dev libpq-dev

# python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# application code
COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]