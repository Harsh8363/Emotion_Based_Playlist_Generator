# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.sentiment_analysis import analyze_sentiment
from src.spotify_recommender import fetch_playlist

app = FastAPI(title="Emotion-Based Playlist Generator API")

class TextInput(BaseModel):
    text: str

@app.post("/analyze/")
def analyze_text(input: TextInput):
    mood, confidence = analyze_sentiment(input.text)
    return {"mood": mood, "confidence": confidence}

@app.get("/playlist/{mood}")
def get_playlist(mood: str):
    playlist_url = fetch_playlist(mood)
    return {"playlist_url": playlist_url}
