# Emotion-Based Playlist Generator 🎶

## 📖 Project Overview
The *Emotion-Based Playlist Generator* analyzes text input to detect the user's mood and recommends Spotify playlists based on the detected emotion. It uses advanced NLP models to perform sentiment analysis and integrates with Spotify's API to provide personalized music recommendations.

---

## 🚀 Features
- 🎤 **Sentiment Analysis** using Hugging Face Transformers  
- 🎧 **Spotify Playlist Recommendation** via Spotify Web API  
- 🖼️ **User-Friendly Interface** using Streamlit  
- 🛠️ **Customizable Sentiment Model** trained with real-world datasets  
- 🌐 **API Integration** with FastAPI for scalable deployment  

---

## 🛠️ Tech Stack

| **Category**    | **Tools/Libraries**                        |
|------------------|----------------------------------------|
| NLP Models       | Hugging Face Transformers, spaCy, NLTK   |
| ML Framework     | TensorFlow / PyTorch                     |
| GenAI Framework  | LangChain                                |
| API Integration  | Spotify Web API, FastAPI                 |
| Web Interface    | Streamlit / Gradio                       |
| Data Sources     | Kaggle, Hugging Face Hub, UCI Repository |

---

## 🏗️ Project Structure

```plaintext
Emotion_Based_Playlist_Generator/
├── app.py                     # Streamlit Application Entry Point
├── requirements.txt           # Required Libraries
├── README.md                  # Project Documentation
├── models/
│   └── sentiment_model.pkl    # Trained Sentiment Analysis Model
├── src/
    ├── train_sentiment_model.py  # Script to Train the Sentiment Model
    ├── spotify_recommender.py    # Spotify Playlist Fetching Logic
    ├── utils.py                  # Utility Functions
    └── __init__.py               # Package Initializer
├── data/
    └── spotify_millsongdata.csv  # Dataset for Sentiment Training
└── .gitignore                 # Ignored Files and Folders
