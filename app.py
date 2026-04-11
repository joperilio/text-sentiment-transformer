from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, validator
from transformers import pipeline
import re

from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
class PredictRequest(BaseModel):
    text: str

    # Basis-Validator erweitern
    @validator("text")
    def not_empty(cls, v):
        # nicht leer
        if not v or not v.strip():
            raise ValueError("Text can not be empty")

        # maximale Länge (z. B. 1000 Zeichen)
        if len(v) > 1000:
            raise ValueError("Text ist too long (max 1000 characters )")

        # erlaubte Zeichen: Buchstaben, Zahlen, Leerzeichen, Satzzeichen
        if not re.match(r"^[\w\s.,!?'-]+$", v):
            raise ValueError("Text contain not allowed special characters")

        return v

# -------------------------------
API_KEY = "supersecretkey"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://bitshawk-technologies.net",
        "http://bitshawk-technologies.net:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
sentiment_pipeline = pipeline("sentiment-analysis")

# -------------------------------
@app.get("/")
def root():
    return {"message": "Transformer Sentiment API"}

@app.post("/predict")
def predict(request: PredictRequest, x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    text = request.text
    result = sentiment_pipeline(text)[0]


    return {
        "sentiment": result["label"],
        "confidence": result["score"]
    }
