from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# -------------------------------
# Request Schema
class PredictRequest(BaseModel):
    text: str

# -------------------------------
app = FastAPI()

# Transformer Sentiment Pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# -------------------------------
@app.get("/")
def root():
    return {"message": "Transformer Sentiment API"}

@app.post("/predict")
def predict(request: PredictRequest):
    # Zugriff auf den Text
    text = request.text
    result = sentiment_pipeline(text)[0]

    return {
        "sentiment": result["label"],
        "confidence": result["score"]
    }