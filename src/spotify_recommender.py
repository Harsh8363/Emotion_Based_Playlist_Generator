# src/spotify_recommender.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def fetch_playlist(mood):
    """
    Fetch a Spotify playlist URL based on the given mood.
    Maps sentiment labels to query keywords and safely checks the API response.
    """
    # Revised mood mapping: try using "feel good" for positive sentiment
    mood_map = {
        "POSITIVE": "feel good",    # Changed from "happy vibes" to "feel good"
        "NEGATIVE": "sad songs",    # Using "sad songs" for negative sentiment
        "NEUTRAL": "chill"
    }
    query = mood_map.get(mood.upper(), "chill")
    print(f"DEBUG: Using query '{query}' for mood '{mood}'")
    
    # Initialize the Spotify API client
    try:
        auth_manager = SpotifyClientCredentials(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        print("Error setting up Spotify client:", e)
        return None

    # Perform the search query
    try:
        results = sp.search(q=query, type='playlist', limit=1)
        print("DEBUG: Spotify API response:", results)
    except Exception as e:
        print("Error calling Spotify API:", e)
        return None

    if not isinstance(results, dict):
        print("DEBUG: Results is not a dictionary.")
        return None

    playlists = results.get("playlists")
    if playlists is None:
        print("DEBUG: 'playlists' key not found in results for query:", query)
        return None

    items = playlists.get("items")
    if not items or not isinstance(items, list):
        print("DEBUG: 'items' list is missing or empty in playlists for query:", query)
        return None

    # Check that the first item is valid
    first_item = items[0]
    if not isinstance(first_item, dict):
        print("DEBUG: The first item in 'items' is not a dictionary for query:", query)
        return None

    external_urls = first_item.get("external_urls")
    if not external_urls or not isinstance(external_urls, dict):
        print("DEBUG: 'external_urls' is missing or not a dictionary in the first item for query:", query)
        return None

    spotify_url = external_urls.get("spotify")
    if not spotify_url:
        print("DEBUG: 'spotify' URL is missing in external_urls for query:", query)
        return None

    return spotify_url
