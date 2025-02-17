import streamlit as st
from src.sentiment_analysis import analyze_sentiment
from src.spotify_recommender import fetch_playlist

st.title("🎶 Emotion-Based Playlist Generator")

user_input = st.text_area("Enter your mood or thoughts:")
if st.button("Generate Playlist"):
    if user_input:
        mood, confidence = analyze_sentiment(user_input)
        st.write(f"Detected Sentiment: **{mood}** (Confidence: {confidence:.2f})")
        playlist_url = fetch_playlist(mood)
        if playlist_url:
            st.markdown(f"[Click here to listen to your playlist]({playlist_url})")
        else:
            st.warning("No playlist found for the detected emotion.")
    else:
        st.warning("Please enter some text!")
