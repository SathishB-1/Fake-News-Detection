# Fake News Detection using Naive Bayes

## Overview

This project is a Fake News Detection system built using the Naive Bayes classification algorithm. It analyzes news articles and predicts whether they are fake or real. The model is deployed as a web application using Streamlit.

## Features

- Preprocessing of news articles (tokenization, stopword removal, etc.)
- Naive Bayes classification model for fake news detection
- User-friendly Streamlit web application
- Interactive interface for testing news articles
- Deployed model for easy access and usage

## Dataset

The dataset used for training the model is obtained from Kaggle and consists of labeled real and fake news articles.

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Natural Language Toolkit (NLTK)
- Naive Bayes (MultinomialNB from scikit-learn)
- Streamlit (for web application)

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage


1. Run the Streamlit web app:

   ```sh
   streamlit run app.py
   ```

2. Enter a news article in the input field to check if it is real or fake.


## Future Enhancements

- Improve model accuracy using deep learning techniques (e.g., LSTM, BERT)
- Provide a confidence score for predictions
- Implement multilingual fake news detection
- Add an explainability module to show reasons behind classification
- Develop an API for integrating the model into other applications
- Enhance the user interface with better visualization and analysis
- Collect and use real-time news data for continuous model updates
- Implement a feedback mechanism for users to improve model performance

## User Interface

![image alt](https://github.com/SathishB-1/Fake-News-Detection/blob/cf9f4c61529f58c41343bd9a79c3a943977dc611/UI.....png)
