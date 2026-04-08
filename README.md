# text-sentiment-transformer

A demo project for text sentiment analysis using FastAPI and Hugging Face Transformers.
It provides a REST API to predict the sentiment of a text (POSITIVE / NEGATIVE) using a pre-trained Transformer model (distilbert-base-uncased-finetuned-sst-2-english). You can run it locally or inside a Docker container.

Features
- REST API to classify text sentiment
- Uses pre-trained Hugging Face Transformers model
- Returns sentiment and confidence score
- Can run locally or in Docker
- Hot-reload for development

---

## Quick Start

### Run locally

```bash
# Install dependencies
pip install fastapi uvicorn transformers

# Start the API - usualy mit dem build und start des container wird ausgeführt
uvicorn app:app --host 0.0.0.0 --port 8000

Access the API at: http://127.0.0.1:8000

### Run with Docker

Build the Docker image:
docker build -t sentiment-transformer .

Run the container
docker run -d -v $(pwd):/app -p 8001:8000 --name sentiment-transformer sentiment-transformer uvicorn app:app --host 0.0.0.0 --port 8000 --reload


API Usage
Endpoint

POST /predict
Content-Type: application/json
Body: {"text": "Your text here"}

Example Requests
curl -X POST http://127.0.0.1:8001/predict \
-H "Content-Type: application/json" \
-d '{"text":"I am not sure if I love this project!"}'

with secret key: 
curl -X POST https://yourserver/predict \ -H "Content-Type: application/json" \ -H "x-api-key: supersecretkey" \
-d '{"text":"Hello"}'

### Development Tips
Use hot reload with uvicorn --reload for fast iteration.
Map local directory in Docker (-v $(pwd):/app) to auto-update code inside container.
Make sure port 8001 (or your chosen port) is open if accessing remotely.


### References
Generate sec keys for https
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -subj "/C=DE/ST=Berlin/L=Berlin/O=Demo/CN=localhost"

### Notes
Recommended Python ≥ 3.8
Docker version ≥ 20.10
Designed as a demo / prototype, not production-ready.

