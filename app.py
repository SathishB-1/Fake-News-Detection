import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import streamlit as st

# Load the model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Initialize lemmatizer and stopwords
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = text.strip()  # Remove leading/trailing spaces
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])  # Lemmatization and stopword removal
    return text

# Prediction function
def predict_fake_news(news_text):
    processed_text = preprocess_text(news_text)
    text_vector = vectorizer.transform([processed_text])
    prediction = model.predict(text_vector)[0]
    return "Fake News" if prediction == 1 else "Real News"

# Streamlit UI
st.title("Fake News Detection")
st.write("Enter a news article below to check if it's real or fake.")

# User input for the news text
news_text = st.text_area("Enter news text here:")

# Prediction and result output
if st.button("Predict"):
    if news_text:
        result = predict_fake_news(news_text)
        st.write(f"### Prediction: {result}")
    else:
        st.warning("Please enter some text to predict.")
