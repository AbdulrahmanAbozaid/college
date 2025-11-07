import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import nltk

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = ' '.join(word for word in text.split() if word not in stop_words)
    text = ' '.join(stemmer.stem(word) for word in text.split())
    return text

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data = data.drop_duplicates()
    data['cleaned_message'] = data['message_content'].apply(preprocess_text)
    return data
