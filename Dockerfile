FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Startbefehl mit SSL
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", \
"--ssl-certfile", "/app/server.crt", "--ssl-keyfile", "/app/server.key", "--reload"]
