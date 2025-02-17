# src/utils.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import logging

nltk.download('punkt')
nltk.download('stopwords')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_text(text):
    """
    Preprocess text: lowercase, tokenize, and remove stopwords/punctuation.
    """
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return ' '.join(tokens)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
