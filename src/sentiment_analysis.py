# src/sentiment_analysis.py
from transformers import pipeline

def analyze_sentiment(text):
    """
    Analyze sentiment using a pre-trained Hugging Face pipeline.
    Returns a tuple: (sentiment_label, confidence_score).
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

