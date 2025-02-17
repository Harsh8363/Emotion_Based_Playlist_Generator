# Emotion‑Based Playlist Generator

## Concept and Vision
This project analyzes user text (e.g., mood descriptions or song lyrics) using sentiment analysis to recommend Spotify playlists and similar songs. It combines cutting‑edge NLP (Hugging Face Transformers, LangChain, OpenAI API) with classical machine learning (TF‑IDF, cosine similarity) to deliver creative and relevant music recommendations.

## Features
- **Sentiment Analysis:** Determines user mood from text input.
- **Playlist Recommendation:** Searches Spotify for playlists matching the detected mood.
- **Song‑Based Recommendation:** Suggests similar songs using a precomputed similarity matrix.
- **Generative Integration:** (Optional) Uses OpenAI (via LangChain) to generate creative playlist descriptions.
- **Deployment:** Uses Streamlit for the UI and FastAPI for scalable API deployment.

## Project Structure
emotion_playlist_generator/
├── app.py                  # Streamlit UI for interactive recommendations
├── model_training.py       # Script to preprocess data and create recommendation model files
├── recommendation.py       # Module containing recommendation functions
├── fastapi_server.py       # FastAPI server exposing API endpoints
├── generator.py            # (Optional) LangChain/OpenAI integration for creative playlist descriptions
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration for deployment
├── README.md               # Project overview, setup, and usage instructions
└── data/
    └── spotify_millsongdata.csv  # Dataset (place your CSV file here)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/emotion_playlist_generator.git
   cd emotion_playlist_generator
