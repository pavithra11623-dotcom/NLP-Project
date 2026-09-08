import streamlit as st
import pickle
import numpy as np
# Load the trained model
model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
# App title
st.title("Sentiment Analysis App")
# User input
user_input = st.text_area("Enter your text here:")
#predict button
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.write("Please enter some text to analyze.")
    else:
        review_vector = vectorizer.transform([user_input])
# Predict sentiment
prediction = model.predict(review_vector)
if st.button("Predict Sentiment"):
    if prediction[0] == 1:
        st.write("The sentiment is: Positive")
    else:
        st.write("The sentiment is: Negative")