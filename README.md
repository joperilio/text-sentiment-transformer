# text-sentiment-transformer

Demo project for **text sentiment analysis** using **FastAPI** and **Hugging Face Transformers**.

- Provides a REST API to predict sentiment of a text (POSITIVE/NEGATIVE).
- Uses a pre-trained Transformer model (`distilbert-base-uncased-finetuned-sst-2-english`).
- Can be run locally or inside a Docker container.

---

## Quick Start

### Run locally

```bash
# Install dependencies
pip install fastapi uvicorn transformers

# Start the API
uvicorn app:app --host 0.0.0.0 --port 8000